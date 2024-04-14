# coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define
from sqlalchemy import and_
from perfcounter import PerfCounterFactory
from config import DOWNTIME, LOG_DIR
from application import Application
import datetime
from utils.mysqlConnect import SessionFactory
from models.machines import Machines
import logging
from handlers.back.getFilterMovies import GetFilterMoviesId

try:
    from cloghandler import ConcurrentRotatingFileHandler as RFHandler
except ImportError:
    from warnings import warn
    warn(
        "ConcurrentLogHandler package not installed.Using builtin log handler")
    from logging.handlers import RotatingFileHandler as RFHandler

define("port", default=9001, help="run on the given port", type=int)
define('log_name',
       default='avatar-cms',
       help='run on the given name',
       type=str)
'''
    初始化系统log
'''


def init_logger(debug=False):
    log_level = debug and logging.DEBUG or logging.INFO
    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = \
        logging.Formatter('[%(asctime)s][module:%(module)s][line:%(lineno)d]'
                          '[%(levelname)s]: %(message)s')

    if RFHandler:
        log_name = "%s/%s.log" % (LOG_DIR, options.log_name)
        handler = RFHandler(log_name,
                            maxBytes=500 * 1024 * 1024,
                            backupCount=100)
        handler.setFormatter(formatter)
        handler.setLevel(log_level)
        logger.addHandler(handler)


'''
    push to falcon
'''


def push():
    perf = PerfCounterFactory.get_or_create()
    perf.push_data_to_proxy()


'''
    定时任务,检查机器的运行状况
    若30min之内没有接收到心跳包,则认为宕机 置status=false time = now()
'''


def check_machines():
    # 获取系统当前时间
    current_time = datetime.datetime.now()
    '''
        查询数据库
        filter条件: Machines.time < current - config["DOWNTIME"]
    '''
    downtime_threshold = current_time - datetime.timedelta(minutes=DOWNTIME)
    session = SessionFactory.getSession()
    try:
        machines = session.query(Machines).filter(
            and_(Machines.time < downtime_threshold, Machines.status == 1)).all()
        if machines:
            for machine in machines:
                machine.status = 0
                machine.time = datetime.datetime.now()
            session.commit()
            logging.warning("New abnormal machine found")
    except Exception as e:
        session.rollback()
        logging.error(
            "Update machines state failed due to database commit error %s", e)

    finally:
        session.close()


# 启动各种定时任务


def time_task():
    tornado.ioloop.PeriodicCallback(GetFilterMoviesId.set_filter_movies,
                                    5 * 60 * 1000).start()
    # 每10分钟启动一次查询数据库的任务,检测是否有异常设备
    tornado.ioloop.PeriodicCallback(check_machines, 10 * 60 * 1000).start()
    # push to falcon 一分钟推送一次
    tornado.ioloop.PeriodicCallback(push, 60 * 1000, jitter=0.1).start()


if __name__ == "__main__":

    tornado.options.parse_command_line()
    init_logger(debug=False)
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    logging.info('Avatar_CMS server listened at port %i ......' % options.port)
    time_task()
    httpServer.start()
    tornado.ioloop.IOLoop.current().start()

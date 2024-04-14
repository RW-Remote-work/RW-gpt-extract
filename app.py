# coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define
from config import DOWNTIME, LOG_DIR
from application import Application
import datetime
import logging
from logging.handlers import RotatingFileHandler as RFHandler

define("port", default=9001, help="run on the given port", type=int)
define('log_name',
       default='rw-gpt-extract',
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



if __name__ == "__main__":

    tornado.options.parse_command_line()
    init_logger(debug=False)
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    logging.info('rw server listened at port %i ......' % options.port)
    httpServer.start()
    tornado.ioloop.IOLoop.current().start()

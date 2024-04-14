import tornado.web
import config
from handlers.backend.extract import GptExtractHandler




class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # 前端页面路由
            # (r'/', findIndexHandler),
            (r'/rw/gpt/extract', GptExtractHandler),  # 查询所有服务器
        ]

        super(Application, self).__init__(handlers, **config.setting)

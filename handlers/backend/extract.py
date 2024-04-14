# -*- coding: utf-8 -*-
# @Time     :  2020/11/25 下午2:46
# @Author   :  liuhang6
# @FileName :  extract.py

import logging
import ujson
from tornado.web import RequestHandler



class GptExtractHandler(RequestHandler):

    def get_post_json_data(self):
        try:
            param = self.request.body.decode('utf-8')
        except Exception as e:
            param = None
            logging.error("parse json data error: %s", e)
        if not param:
            return ''
        return ujson.loads(param)

    def get(self):
        '''
        :return:
        '''
        return self._handle_request()

    def post(self, *args, **kwargs):
        '''
        :return:
        '''
        return self._handle_request()
    

    @property
    def tips(self):
        """
        get tips from json
        """
        return self.get_post_json_data.get("tips", [])

    @property
    def input_html(self):
        return self.get_post_json_data.get("input", '')

    def get(self):
        res = {}
        self.write(res)
        self.flush()

    def post(self):
        data = self.get_post_json_data
        if not data:
            logging.error("filter packet empty")
            return self.write(dict(retCode=20002, msg="请求参数不能为空"))
        method = self.method
        if not method:
            return self.write(dict(retCode=20002, msg="请求方法名不能为空"))
        if not hasattr(self, method):
            self.write(dict(retCode=20001, msg="请求方法不存在"))
        else:
            result = getattr(self, method)()
            self.sendResponseWithoutData(result)


    def sendResponseWithoutData(self, response):
        self.write({
            "retCode": response.get("retCode"),
            "msg": response.get("msg"),
        })
        self.flush()

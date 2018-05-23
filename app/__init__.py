# -*- coding: utf-8 -*-


from flask import jsonify


class RestResponse(object):
    """ 标准的接口Response类, 所有的api必须返回这个类的对象, 以便统一处理返回 """

    def __init__(self, language=None):
        self.language = language or "en"

    def fail(self, code=500, message="Server Got A Exception"):
        d = {'meta': {
            'success': False, 'status_code': code,
            'message': message
        }}
        json_response = jsonify(d, )
        return json_response

    def success(self, code=200, data=None):
        d = {'meta': {
            'success': True, 'status_code': code,
            'message': "Requset Successes"
        }, 'data': data}
        json_response = jsonify(d)
        return json_response

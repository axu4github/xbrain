# coding=utf-8

from xbrain.loggings import LoggableMixin

import json


SUCCESS = 0
FAILED = -99


class Response(LoggableMixin):

    def __init__(self, message, status, context, *args, **kwargs):
        super(Response, self).__init__(*args, **kwargs)
        self.message = message
        self.status = status
        self.context = context

    def __str__(self):
        return json.dumps({
            "status": self.status,
            "message": self.message,
            "response": self.context
        })


class SuccessResponse(Response):

    def __init__(self, message=None, status=SUCCESS, *args, **kwargs):
        super(SuccessResponse, self).__init__(
            message=None, status=SUCCESS, *args, **kwargs)


class FailedResponse(Response):
    def __init__(self, message=None, status=FAILED, *args, **kwargs):
        super(SuccessResponse, self).__init__(
            message=None, status=SUCCESS, *args, **kwargs)

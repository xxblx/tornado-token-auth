import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    @property
    def executor(self):
        return self.application.executor

    @property
    def hmac_key(self):
        return self.application.hmac_key

    def raise_error(self, status_code, message):
        self.raise_status(status_code, {'message': message})

    def raise_status(self, status_code=200, payload=None):
        self.clear()
        self.set_status(status_code)
        if payload:
            self.write(payload)
        self.finish()

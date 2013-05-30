import tornado.ioloop
import tornado.web
from tornado.escape import json_decode
import xlsx_factory


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        content_type = self.request.headers.get("Content-Type", "")
        if content_type.startswith("application/json"):
            input = json_decode(self.request.body)
            result = xlsx_factory.create(input)
            self.write(result)
        else:
            self.write("content_type should be set to application/json")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(12345)
    tornado.ioloop.IOLoop.instance().start()
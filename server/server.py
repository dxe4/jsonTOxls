import tornado.ioloop
import tornado.web
from tornado.escape import json_decode
import traceback, sys
import xlsx_factory
from input_factory import InputHandler


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        content_type = self.request.headers.get("Content-Type", "")
        if content_type.startswith("application/json"):
            try:
                input = json_decode(self.request.body)
                result = xlsx_factory.create(input)
                self.write(result)
            except Exception as e:
                self.write("".join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])))
        else:
            self.write("content_type should be set to application/json")


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(12345)
    tornado.ioloop.IOLoop.instance().start()
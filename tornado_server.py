import tornado.ioloop
import tornado.web
from tornado.escape import json_decode
import xlsxFactory
from collections import OrderedDict

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        content_type = self.request.headers.get("Content-Type", "")
        if content_type.startswith("application/json"):
            sheet_list = json_decode(self.request.body)
            result = xlsxFactory.create(sheet_list)
            self.write(result)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(12345)
    tornado.ioloop.IOLoop.instance().start()
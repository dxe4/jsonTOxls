import tornado.ioloop
import tornado.web
from tornado.escape import json_decode
import xlsxFactory
from collections import OrderedDict

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        content_type = self.request.headers.get("Content-Type", "")
        if content_type.startswith("application/json"):
            dict = json_decode(self.request.body)
            sorted_dict= OrderedDict(sorted(dict.items(), key=lambda t: t[0]))
            result = xlsxFactory.create(sorted_dict)
            self.write(result)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(12345)
    tornado.ioloop.IOLoop.instance().start()
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web

from tornado.options import define,options
define('port',default='8888',help='run on the given port',type=int)

from urls import url
from config import settings

class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self,url,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
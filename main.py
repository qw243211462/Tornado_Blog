import MySQLdb
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
import os

from tornado.options import define,options
define('port',default='8888',help='run on the given port',type=int)
define('mysql_host',default="localhost", help="database host")
define('mysql_user',default='tong@Tong',help="database user")
define('mysql_password',default="qw13198321328", help="database password")
define('mysql_database',default="blog", help="database name")

from handlers import index,auth,articles,design,SumArticles

class Application(tornado.web.Application):

    def __init__(self):
        setting = dict(
            template_path = os.path.join(os.path.dirname(__file__),'templates'),
            static_path = os.path.join(os.path.dirname(__file__),'static'),
            xsrf_cookies=False,
            cookie_secret="RYxFqFQyRCiCZ/nxFfTMCrbqZpRZ5UW9tQ86fKvrfIw=",
            debug=True,
        )
        handlers = [ (r'/',index.IndexHandler),
                     (r'/register',auth.RegisterHandler),
                     (r'/login',auth.LoginHandler),
                     (r'/blog/index/(?P<page_num>\d*)',index.BlogIndexHandler),
                     (r'/blog/articles/(?P<article_id>\d*)',articles.ArticleHandler),
                     (r'/blog/design', design.designHandler),
                     (r'/blog/articles/(?P<year>\d*)/(?P<month>\d*)',SumArticles.SumArticlesHandler)
                     #(r'/blog/articles/(?P<article_id>.*)/(?P<comments_id>.*)',articles.CommentsHandler),
                ]
        tornado.web.Application.__init__(self,handlers,**setting)
        self.db = MySQLdb.Connection(
            host='127.0.0.1',
            database='blog',
            user='root',
            password='qw13198321328',
            charset = 'utf8'
        )



if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
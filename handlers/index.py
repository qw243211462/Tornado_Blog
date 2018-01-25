import tornado.web
from handlers import BaseHandler
import string

class IndexHandler(BaseHandler.BaseHandler):
    def get(self):
        self.write('hello world')

class BlogIndexHandler(BaseHandler.BaseHandler):
    def get(self):
        cur = self.db.cursor()
        sql = 'select id,article_title,article_time from articles ORDER BY rand() limit 5'
        info = cur.execute(sql)
        info1 = cur.fetchall()
        id_list = []
        titles_list = [] #标题
        date_list = [] #日期
        for id,title,time in info1:
            id_list.append(str(id).strip(string.punctuation))
            titles_list.append(str(title).strip(string.punctuation))
            date_list.append(time)
        self.render('blog/index.html',titles_list = titles_list,date_list = date_list,
                    id_list = id_list)
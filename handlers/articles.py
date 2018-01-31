from handlers import BaseHandler
import tornado.web
import string
import datetime
import json

class ArticleHandler(BaseHandler.BaseHandler):
    def get(self,article_id):
        article_id = article_id
        cur =self.db.cursor()
        sql = "select article_title,article_content,article_time  from articles where id=%s"%(article_id)
        info = cur.execute(sql)
        info1 = cur.fetchone()


        #name = self.get_argument('')


        self.render('blog/article.html',article_content = str(info1[1]).strip(string.punctuation),
                    article_title = str(info1[0]).strip(string.punctuation),
                    article_time = str(info1[2])
                    )

    def post(self,article_id):
        user_name = self.get_argument("user_name")
        current_date = self.get_argument('current_date')
        content = self.get_argument("content", None)
        resvalue = {'user_name':[user_name,],
                    'current_date':[current_date,],
                    'content': [content, ],}
        self.write(json.dumps(resvalue))



class CommentsHandler(BaseHandler.BaseHandler):
    def get(self):
        self.write('hello world')

    def post(self):
        self.write('heelo world')
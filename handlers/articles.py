from handlers import BaseHandler
import tornado.web
import string

class ArticleHandler(BaseHandler.BaseHandler):
    def get(self,article_id):
        article_id = article_id
        cur =self.db.cursor()
        sql = "select article_title, article_content from articles where id=%s"%(article_id)
        info = cur.execute(sql)
        info1 = cur.fetchone()
        self.render('blog/article.html',article_content = str(info1[1]).strip(string.punctuation),
                    article_title = str(info1[0]).strip(string.punctuation))

class CommentsHandler(BaseHandler.BaseHandler):
    def get(self):
        self.write('hello world')

    def post(self):
        self.write('heelo world')
import tornado.web
from handlers import BaseHandler
import string

class IndexHandler(BaseHandler.BaseHandler):
    def get(self,page_num):
        self.write('hello world')

class BlogIndexHandler(BaseHandler.BaseHandler):
    def get(self,page_num):
        cur = self.db.cursor()
        sql = 'select id,article_title,article_time from articles ORDER BY rand()'
        info = cur.execute(sql)
        info1 = cur.fetchall()
        id_list = [] #文章id
        titles_list = [] #标题
        date_list = [] #日期

        for id,title,time in info1:
            id_list.append(str(id).strip(string.punctuation))
            titles_list.append(str(title).strip(string.punctuation))
            date_list.append(time)

        try:
            page_num = int(page_num)
        except:
            page_num = 1
        if page_num <= 0:
            page_num = 1

        start = (page_num - 1) * 5
        end = page_num * 5
        current_id = id_list[start:end]
        current_title = titles_list[start:end]
        current_date = date_list[start:end]

        all_pager, c = divmod(info, 5)
        self.render('blog/index.html',current_title = current_title,current_date = current_date,
                    current_id = current_id,all_pager = all_pager)



##实现文章归档
from handlers import BaseHandler
import MySQLdb
import string
import time as time1

class SumArticlesHandler(BaseHandler.BaseHandler):
    def get(self,year,month):
        year = year
        month = month
        cur = self.db.cursor()
        sql = "select id,article_title,article_time from articles where date_format(article_time,'%%Y-%%m')='%s-%s'" % (year, str(month).zfill(2))
        info = cur.execute(sql)
        info1 = cur.fetchall()

        id_list = []  # 文章id
        titles_list = []  # 标题
        date_list = []  # 日期

        for id, title, time in info1:
            id_list.append(str(id).strip(string.punctuation))
            titles_list.append(str(title).strip(string.punctuation))
            date_list.append(time)

            #   归档时间处理
            date = time1.strftime('%Y-%m-%d')
            year = date[0:4]
            month = date[5:7]
            if month[0] != 0:
                month = month
            else:
                month = month[1]
            month_list = []
            year_list = []
            for i in range(int(month)):
                month_list.append(i)
                year_list.append(int(year))

        self.render('blog/sumArticles.html',id_list = id_list,titles_list = titles_list,
                    date_list = date_list,year_list = year_list,month_list = month_list)

    def post(self):
        pass
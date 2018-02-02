from handlers import BaseHandler
import string
import json
import datetime


##datetime.datetime is not JSON serializable 报错问题解决
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self,obj)

class designHandler(BaseHandler.BaseHandler):
    def get(self):
        cur = self.db.cursor()
        sql = 'select id,article_title,article_time from articles ORDER BY rand() limit 10'
        info = cur.execute(sql)
        info1 = cur.fetchall()
        id_list = []  # 文章id
        titles_list = []  # 标题
        date_list = []  # 日期

        for id, title, time in info1:
            id_list.append(str(id).strip(string.punctuation))
            titles_list.append(str(title).strip(string.punctuation))
            date_list.append(time)
        self.render('blog/design.html', titles_list=titles_list, date_list=date_list,
                    id_list=id_list)

    def post(self, *args, **kwargs):
        cur = self.db.cursor()
        sql = 'select id,article_title,article_time from articles ORDER BY rand() limit 5'
        info = cur.execute(sql)
        info1 = cur.fetchall()
        id_list = []  # 文章id
        titles_list = []  # 标题
        date_list = []  # 日期

        for id, title, time in info1:
            id_list.append(str(id).strip(string.punctuation))
            titles_list.append(str(title).strip(string.punctuation))
            date_list.append(time)
        resvalue = {"title":[
            {
                "id":id_list[0],
                "title":titles_list[0],
                "date":date_list[0],
            },
            {
                "id":id_list[1],
                "title":titles_list[1],
                "date":date_list[1]
            },
            {
                "id": id_list[2],
                "title": titles_list[2],
                "date": date_list[2]
            },
            {
                "id": id_list[3],
                "title": titles_list[3],
                "date": date_list[3]
            },
            {
                "id": id_list[4],
                "title": titles_list[4],
                "date": date_list[4]
            },
        ]}
        self.write(json.dumps(resvalue,cls=DateEncoder))
from datetime import date,datetime
import json
import tornado.web
import tornado.gen

class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def gete_current_user(self):
        '''
        获取当前用户
        '''
        return self.get_secure_cookie('user')


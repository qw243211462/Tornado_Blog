import tornado.web
import datetime
from handlers import BaseHandler

class RegisterHandler(BaseHandler.BaseHandler):
    '''
     注册处理类
    '''

    def get(self):
        self.render('register.html')


    def post(self):
        username = self.get_body_argument('input_user', default='')
        email = self.get_body_argument('input_email',default='')
        password = self.get_body_argument('input_password',default='')

        # 判断用户名或者邮箱是否已被使用
        if not self._checkusername_action(username, email):
            cur = self.db.cursor()
            #sql = "insert into user(user_name,user_email,user_password) VALUES ('wangmao','123456@qq.com','123456')"
            sql = "insert into user(user_name,user_email,user_password) VALUES ('%s','%s','%s')"%(username,email,password)
            cur.execute(sql)
            cur.close()
            self.db.commit()
            self.db.close()
            self.redirect('/')
        else:
            self.write('error')

    def _checkusername_action(self,username, email):
        '''
                 检查是否有该用户
        '''
        cur = self.db.cursor()
        sql = "select id from user where (user_name='%s' or user_email='%s')" %(username,email)
        user_number = cur.execute(sql)
        if user_number == 0:
            return False
        else:
            return True

class LoginHandler(BaseHandler.BaseHandler):
    '''
     登录处理类
    '''
    def get(self):
        self.render('login.html')


    def post(self):
        username = self.get_body_argument("input_user")
        passwd = self.get_body_argument("input_password")
        print(username,passwd)

        if self._checkuser_action(username):
            if self._checkpasswd_action(username,passwd):
                self.redirect("blog/index")
            else:
                self.write('password error')
        else:
            self.write('user error')

    def _checkuser_action(self,username):
        '''
         检查是否有该用户
        '''
        cur = self.db.cursor()
        sql_user = "select id from user where (user_name='%s')"%(username)
        user_number = cur.execute(sql_user)
        if user_number == 0:
            return False
        else:
            return True

    def _checkpasswd_action(self,username,password):
        '''
                检查用户密码是否正确
        '''
        cur =self.db.cursor()
        sql_passwd = "select id,user_name from user WHERE (user_name='%s'and user_password='%s')"%(username,password)
        user_number = cur.execute(sql_passwd)
        if user_number == 0:
            return False
        else:
            return True

import tornado.web
import config
from handlers import index

url = [(r'/',index.IndexHandler)]
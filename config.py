import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    static_path = os.path.join(os.path.dirname(__file__),'static'),
    xsrf_cookies=True,
    cookie_secret="RYxFqFQyRCiCZ/nxFfTMCrbqZpRZ5UW9tQ86fKvrfIw=",
    debug=True,
)
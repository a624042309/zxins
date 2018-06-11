# -*- coding: utf-8 -*-
from app.blog.blog_config import app_port

bind = "0.0.0.0:{port}".format(port=app_port)
workers = 1
worker_class = "gevent"
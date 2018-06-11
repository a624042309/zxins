# -*- coding: utf-8 -*-

from app.blog.views.index import *
from app.blog.blog_config import app, app_host, app_port

if __name__ == '__main__':
    app.run(host=app_host, port=int(app_port))

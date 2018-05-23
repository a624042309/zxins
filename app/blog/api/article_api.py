# -*- coding: utf-8 -*-

from flask import jsonify, render_template
from app.blog.blog_config import app
from app.blog.application.contro.controller import Controller


@app.route('/', methods=['GET'])
def posts():
    cl = Controller()
    articles = cl.get_all_article()
    d = {'articles': []}
    d['articles'] = [article.dictify() for article in articles]
    return render_template('index.html', posts=articles)

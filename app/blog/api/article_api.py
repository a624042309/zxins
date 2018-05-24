# -*- coding: utf-8 -*-

from schemer import Schema
from flask import jsonify, render_template, request
from app.blog.blog_config import app
from app.blog.application.contro.controller import Controller


@app.route('/', methods=['GET'])
def index():
    cl = Controller()
    article_list = cl.get_all_article()

    return render_template('index.html', article_list=article_list)


@app.route('/detail/<no>', methods=['GET'])
def detail(no):
    cl = Controller()
    article = cl.get_one_article(**dict(no=no))

    return render_template('detail.html', article=article)

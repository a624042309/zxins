# -*- coding: utf-8 -*-

from schemer import Schema
from flask import jsonify, render_template, request
from app.blog.blog_config import app
from app.blog.application.contro.controller import Controller


@app.route('/', methods=['GET'])
def index():
    # cl = Controller()
    # article_list = cl.get_all_article()
    return render_template('index.html', imgs=[1,2,3])


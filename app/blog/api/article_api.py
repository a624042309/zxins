# -*- coding: utf-8 -*-

from schemer import Schema
from flask import jsonify, render_template, request
from app.blog.blog_config import app
from app.blog.application.contro.controller import Controller


@app.route('/', methods=['GET'])
def index():
    cl = Controller()
    article_list = cl.get_all_article()
    # d = {'articles': []}
    # d['articles'] = [article.dictify() for article in article_list]
    return render_template('index.html', article_list=article_list)


@app.route('/detail', methods=['POST'])
def detail(**kwargs):
    params = request.get_json(silent=True)
    param_schema = Schema({
        'no': {'type': basestring, 'required': True},
    }, strict=False)

    param_schema.validate(params)  # 检测不通过直接抛异常
    param_schema.apply_defaults(params)  # attach 默认值

    cl = Controller()
    article = cl.get_one_article(**kwargs)

    return render_template('detail.html', article=article)

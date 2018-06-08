# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for
from app.blog.blog_config import app
from app.blog.controller.forms import EditorForm
from app.blog.controller.controller import Controller


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', imgs=[1, 2, 3])


@app.route('/write', methods=('GET', 'POST'))
def write():
    form = EditorForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        param = {
            'title': title,
            'content': content,
        }
        con = Controller()
        con.create_article(param)
        return render_template('preview.html', title=title, content=content)
    return render_template('editor.html', form=form)


@app.route('/article', methods=['POST'])
def article():
    return ''

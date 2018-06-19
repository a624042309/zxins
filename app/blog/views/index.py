# -*- coding: utf-8 -*-

from flask import render_template
from app.blog.blog_config import app
from app.blog.controller.forms import EditorForm
from app.blog.controller.controller import Controller


@app.route('/', methods=['GET'])
def index():
    con = Controller()
    hot = con.find_hot()
    items = con.find_all()
    return render_template('index.html', hot=hot, items=items)


@app.route('/write', methods=('GET', 'POST'))
def write():
    form = EditorForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        intro = form.intro.data
        param = {
            'title': title,
            'content': content,
            'intro': intro,
        }
        con = Controller()
        article = con.create_article(param)
        return render_template('article.html', article=article)
    return render_template('editor.html', form=form)


@app.route('/article/<id>', methods=['GET', 'POST'])
def article(id):
    con = Controller()
    article = con.find_with_info(id=id)
    return render_template('article.html', article=article)


@app.route('/video')
def video():
    return render_template('video.html')
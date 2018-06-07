# -*- coding: utf-8 -*-

from flask import render_template, redirect, request
from app.blog.blog_config import app
from app.blog.controller.forms import UserForm

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', imgs=[1,2,3])

@app.route('/write', methods=('GET', 'POST'))
def write():
    form = UserForm()
    if form.validate_on_submit():
        account = request.form.get('account')
        passwd = request.form.get('passwd')


        return redirect('/')
    return render_template('editor.html', form=form)
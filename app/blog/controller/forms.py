# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    account = StringField(u'用户名:', validators=[DataRequired()])
    passwd = StringField(u'密码:', validators=[DataRequired()])
    submit = SubmitField(u'登录')

class EditorForm(FlaskForm):
    title = StringField(u'标题:', validators=[DataRequired(u'请输入标题.')])
    intro = StringField(u'简介:')
    content = TextAreaField(u'内容:', validators=[DataRequired(u'请输入内容.')])
    submit = SubmitField(u'提交')
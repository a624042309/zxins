# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    account = StringField(u'用户名:', validators=[DataRequired()])
    passwd = StringField(u'密码:', validators=[DataRequired()])

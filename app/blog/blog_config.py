# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.secret_key = 'key secret zxins'
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
# enable markdown plugin
app.config['CKEDITOR_ENABLE_MARKDOWN'] = True

Bootstrap(app)
ckeditor = CKEditor(app)

app_host = '0.0.0.0'
app_port = '5000'

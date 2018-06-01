# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app_host = '0.0.0.0'
app_port = '5000'

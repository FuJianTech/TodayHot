#! /usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask,render_template
from flask_cors import *  # 导入模块
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域

from  app.applications.applications_hot import hot # 热点
app.register_blueprint(hot,url_prefix='/hot')

from app.daily_code.views import codes # 常用函数
app.register_blueprint(codes,url_prefix='/codes')


@app.route('/')
def index():
	return  render_template("index.html")


app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    port = 5001
    host='0.0.0.0'
    # host = '127.0.0.1'
    app.run(debug=False, host=host, port=port)

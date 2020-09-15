#! /usr/bin/env python
# -*-coding:utf-8-*-
import  sys,os
from flask import Flask,render_template
from flask_cors import *  # 导入模块
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域

# 加入app路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from TodayHot.app.applications.applications_hot import hot  # 热点
app.register_blueprint(hot, url_prefix='/hot')

from app.daily_code.views import codes  # 常用函数
app.register_blueprint(codes, url_prefix='/codes')


@app.route('/')
def index():
    return render_template("hotpress.html")


# 返回字符串不乱码
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    port = 5000
    host = '0.0.0.0'
    # host = '127.0.0.1'
    app.run(debug=True, host=host, port=port)

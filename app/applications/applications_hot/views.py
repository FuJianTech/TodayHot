#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import jsonify
from TodayHot.app.applications.applications_hot import hot
from TodayHot.app.applications.applications_hot.fun import Hot

@hot.route("/get_weibo_hot", methods=["POST", "GET"])
def get_weibo_hot():
    ht  = Hot()
    result = json.dumps(ht.weibo_zhihu()[1])
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})

@hot.route("/get_zhihu_hot", methods=["POST", "GET"])
def get_toutiao_hot():
    result = json.dumps(Hot().weibo_zhihu()[0])
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})

@hot.route("/get_baidu_hot", methods=["POST", "GET"])
def get_baidu_ho():
    result = Hot().hot_baidu()
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})

@hot.route("/get_key_word/", methods=["POST", "GET"])
def get_key_word():
    result = Hot().key_word()[0]
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})

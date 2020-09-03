#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import jsonify
from app.applications.applications_hot import hot
from app.applications.applications_hot.fun import Hot


@hot.route("/get_weibo_hot", methods=["POST", "GET"])
def get_weibo_hot():
    ht = Hot()
    result = ht.hot_weibo()
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})


@hot.route("/get_baidu_hot", methods=["POST", "GET"])
def get_baidu_ho():
    ht = Hot()
    result = ht.hot_baidu()
    print(type(result))
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})


@hot.route("/get_zhihu_hot", methods=["POST", "GET"])
def get_zhihu_hot():
    ht = Hot()
    result = ht.hot_zhihu()
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})


@hot.route("/get_douyin_hot/", methods=["POST", "GET"])
def get_douyin_hot():
    ht = Hot()
    result = ht.hot_douyin()
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})


@hot.route("/get_toutiao_hot/", methods=["POST", "GET"])
def get_toutiao_hot():
    ht = Hot()
    result = ht.hot_toutiao()
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})


@hot.route("/get_sort_hot/", methods=["POST", "GET"])
def get_sort_hot():
    ht = Hot()
    result = ht.hot_sort()
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})

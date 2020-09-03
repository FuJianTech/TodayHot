# !/bin/env python
# -*- coding=utf-8 -*-

import sys
sys.path.append(r'/home/xqkj/')

from app.daily_code.fun import multiple_hot_json
from app.applications.applications_hot import Hot


baidu_json = eval(Hot().hot_baidu())
weibo_json = eval(Hot().hot_weibo())
zhihu_json = (Hot().hot_zhihu())


multiple_hot_json(baidu_json, "百度")
multiple_hot_json(baidu_json, "微博")
multiple_hot_json(zhihu_json, "知乎")

# try:
#     douyin_json=eval(Hot().hot_douyin())
#     toutiao_json=eval(Hot().hot_toutiao())
#
#     multiple_hot_json(douyin_json,"抖音")
#     multiple_hot_json(toutiao_json, "头条")
# except:
#     pass


#

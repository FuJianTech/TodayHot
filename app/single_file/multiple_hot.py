# !/bin/env python
# -*- coding=utf-8 -*-

# root路径写在 manager.py中,此版本#sys勿删，下版本删除或者更新
# import sys
# # sys.path.append(r'/home/FuJianTech/TodayHot')  linux
# sys.path.append(r'E:\FuJianTech\TodayHot')  # 修改为自己的目录

from TodayHot.app.daily_code.fun import multiple_hot_json
from TodayHot.app.applications.applications_hot.fun import Hot

# 解析
baidu_json = eval(Hot().hot_baidu())
weibo_json = Hot().weibo_zhihu()[1]
zhihu_json = Hot().weibo_zhihu()[0]

# 存储
multiple_hot_json(baidu_json, "百度")
multiple_hot_json(baidu_json, "微博")
multiple_hot_json(zhihu_json, "知乎")


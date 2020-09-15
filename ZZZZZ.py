#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  sys

import os
import sys

win32 = sys.platform.startswith('win')

if win32:
    # print(sys.executable)
    sub_path, file_name = os.path.split(sys.executable)
print(sub_path)
print(file_name)

import  json
res2 = {"关键字一号":"123","key2":"abc"}
res2_json = json.dumps(res2,indent=4,ensure_ascii=False) #indent 左边空格4个字符，格式化json内容
print(res2_json)


data   = root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
print(root_path)

data = sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

print(data)
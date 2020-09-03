#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

hot = Blueprint("hot", __name__)

from .views import *  # 使注册的蓝图可以找到views下面的路由


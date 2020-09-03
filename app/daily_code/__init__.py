from flask import Blueprint
codes = Blueprint("code", __name__)
from .views import *  # 使注册的蓝图可以找到views下面的路由
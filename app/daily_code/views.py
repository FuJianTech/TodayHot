from . import codes  # 蓝图引用进来
from .fun import select_data_dict
from flask import jsonify


@codes.route('/detail', methods=['GET', 'POST'])
def detail():
    return 'detail'


@codes.route('/A', methods=['GET', 'POST'])
def detail1():
    return 'B'


@codes.route('/eecode_to_word/<path:data>/', methods=['GET', 'POST'])
def use_path(data):  # 返回值  123213213

    res = 1
    return str(res)


@codes.route('/select_data_dict')  # 140
def select_data_dict():
    # 运行修改sql配置文件
    from app.daily_code.fun import select_data_dict
    result = select_data_dict()
    return jsonify({"rescode": 0, "resmsg": "success", "data": result})

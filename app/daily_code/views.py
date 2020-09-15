from . import codes  # 蓝图引用进来

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


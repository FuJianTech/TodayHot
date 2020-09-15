# 用来写逻辑
# !/bin/env python
# -*- coding=utf-8 -*-
import pymysql
import os
import datetime
import configparser
import paddlehub as hub
import uuid
class Mysql_link(object):
    # 初始化数据库配置
    def __init__(self, cfg_sql_file):

        cfg_sql_file = oper_sys(cfg_sql_file)
        print(19, cfg_sql_file) # 保留

        self.ip = cfg("mysql_hot", "ip", cfg_sql_file)  #
        self.name = cfg("mysql_hot", "name", cfg_sql_file)
        self.password = cfg("mysql_hot", "pw", cfg_sql_file)
        self.db = cfg("mysql_hot", "db", cfg_sql_file)  # 数据库名称
        self.port = int(cfg("mysql_hot", "port", cfg_sql_file))

    def select_mysql(self, sql):

        db = pymysql.connect(
            self.ip,
            self.name,
            self.password,
            self.db,
            self.port)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()
        return data

    # 新增数据
    def insert_mysql(self, sql):
        db = pymysql.connect(
            self.ip,
            self.name,
            self.password,
            self.db,
            self.port)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            print("數據存儲成功")
        except Exception as e:
            print(e)
            db.rollback()
        db.close()

def cfg(config_name, para, file_path):
    config = configparser.ConfigParser()  # 类实例化
    config.read(file_path)
    value = config[config_name][para]
    return value

def paddle_fenci(content):
    lac = hub.Module(name='lac')
    test_text = []
    test_text.append(content)
    inputs = {"text": test_text}
    results = lac.lexical_analysis(data=inputs)
    results_list = [
        "LOC",
        "PER",
        "ORG",
        "nr",
        "ns",
        "nz",
        "nt",
        "nw",
        "vn",
        "n"]
    for result in results:
        for i in result["tag"]:
            for j in results_list:
                if i == j:
                    num = result["tag"].index(i)
                    print(result["word"][num])
                    if len(result["word"][num]) < 10:
                        return result["word"][num]

def multiple_hot_json(hot_json, hot_name):
    # 解析json，存储带数据库
    for key, value in hot_json.items():
        key = repr(key)
        for i in range(len(hot_json)):
            ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
        datatime = repr(
            str(ts).replace(
                "-",
                "").replace(
                " ",
                "").replace(
                ":",
                ""))
        category = repr(hot_name)
        collect_time = datetime.datetime.now().strftime('%Y-%m-%d')
        collect_time = repr(collect_time)
        uu = uuid.uuid4()
        key_word = repr(paddle_fenci(value))
        uu = repr(str(uu))
        value = repr(value)

        sql = f'INSERT INTO baidu_hot(id,content,timez,category,collect_time,uuid,key_word) VALUES({key},{value},{datatime},{category},{collect_time},{uu},{key_word})'
        print(sql + ";") # 保留，检测sql语句
        sql_file_name = r'/app/sql_files/sql_aliyun_2499_hot.ini'
        sql_file_name = three_path(sql_file_name)
        MQ = Mysql_link(sql_file_name)
        MQ.insert_mysql(sql)

def oper_sys(cfg_sql_file):
    if os.name == "nt":
        sql_file_name = cfg_sql_file.replace("\\", "\\\\").replace("/", "\\\\")
        return sql_file_name

    if os.name == "posix":
        sql_file_name = cfg_sql_file.replace("\\", "/")
        print(sql_file_name)
        return sql_file_name

def three_path(path):
    current_path = os.path.dirname(__file__)
    # 上一级路径（父级路径）
    parent_path = os.path.dirname(current_path)
    tr_path = os.path.dirname(parent_path)
    join_file_name = tr_path + path
    return join_file_name

if __name__ == '__main__':
    # 测试，保留
    sql_file_name = r'/app/sql_files/sql_local_test.ini'
    sql_file_name = three_path(sql_file_name)
    MQ = Mysql_link(sql_file_name)
    MQ.select_mysql("SELECT VERSION()")
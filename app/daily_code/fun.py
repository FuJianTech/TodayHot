# 用来写逻辑
# !/bin/env python
# -*- coding=utf-8 -*-
import pymysql
import os
import datetime
# mysql
class Mysql_link(object):
    # 初始化数据库配置
    def __init__(self,cfg_sql_file):

        cfg_sql_file =oper_sys(cfg_sql_file)
        print(19,cfg_sql_file)

        self.ip = cfg("mysql_hot", "ip", cfg_sql_file)  #
        self.name = cfg("mysql_hot", "name", cfg_sql_file)
        self.password = cfg("mysql_hot", "pw", cfg_sql_file)
        self.db = cfg("mysql_hot", "db", cfg_sql_file)  # 数据库名称



    def select_mysql(self,sql):
        db=pymysql.connect(self.ip, self.name, self.password, self.db)
        cursor=db.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()
        db.close()

        return data

    # 新增数据
    def insert_mysql(self, sql):
        db=pymysql.connect(self.ip, self.name, self.password, self.db)
        cursor=db.cursor()
        # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
            cursor.execute(sql)
            db.commit()
            print("數據存儲成功")
        except Exception  as  e:
            print(e)
            db.rollback()
        db.close()


def cfg(config_name,para,file_path):
    # 导包
    import configparser
    config=configparser.ConfigParser()  # 类实例化
    config.read(file_path)
    value=config[config_name][para]
    return value


def multiple_hot_json(hot_json, hot_name):
    # 解析json，存储带数据库
    for key, value in hot_json.items():
        key=repr(key)
        value=repr(value)
        for i in range(len(hot_json)):

            ts=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
            ts=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
        datatime=repr(str(ts).replace("-", "").replace(" ", "").replace(":", ""))
        category=repr(hot_name)

        collect_time = datetime.datetime.now().strftime('%Y-%m-%d')
        collect_time = repr(collect_time)
        sql=f'INSERT INTO baidu_hot(id,content,timez,category,collect_time) VALUES({key},{value},{datatime},{category},{collect_time})'
        print(sql + ";")
        sql_file_name = r'/app/sql_files/sql_aliyun_2499_hot.ini'
        sql_file_name = three_path(sql_file_name)
        MQ = Mysql_link(sql_file_name)
        MQ.insert_mysql(sql)


def select_data_dict():
    # 重组字典
    sql_file_name = r'/app/sql_files/sql_local_test.ini'
    sql_file_name = three_path(sql_file_name)
    MQ = Mysql_link(sql_file_name)
    selec_sql = "SELECT distinct c.DEPARTMENT FROM `command_table` c"
    # selec_sql2 = "SELECT distinct c.OFFICE FROM `command_table` c where c.DEPARTMENT = 'kk'"
    res_one = MQ.select_mysql(selec_sql)  # 筛选数据
    res_one = list(res_one)
    one_dict = {}
    for i in res_one:
        one = "".join(i)
        selec_sql2 = "SELECT distinct c.OFFICE FROM command_table c where c.DEPARTMENT ='" + one + "'"
        res_two = MQ.select_mysql(selec_sql2)  # 筛选数据
        office_dict = {}
        for j in res_two:
            two_list = []
            two = "".join(j)
            selec_sql3 = "select c.`*` FROM command_table c WHERE c.DEPARTMENT ='" + one + "'  and c.OFFICE ='" + two + "'"
            res_three = MQ.select_mysql(selec_sql3)  # 筛选数据
            for k in res_three:
                three_dict = {}
                three_dict["OBJECT"] = k[0]
                three_dict["NAME"] = "".join(k[4])  # 名字
                three_dict["POST"] = k[5]  #
                three_dict["PHONENUMBER"] = k[6]  #
                three_dict["OFFICETELEPHONE"] = k[7]  #
                two_list.append(three_dict)
            office_dict[two] = two_list
        one_dict[one] = office_dict
    return  one_dict



def oper_sys(cfg_sql_file):
    import os
    if os.name == "nt":
        sql_file_name = cfg_sql_file.replace("\\", "\\\\").replace("/", "\\\\")
        return  sql_file_name

    if os.name == "posix":
        sql_file_name = cfg_sql_file.replace("\\", "/")
        print(sql_file_name)
        return  sql_file_name


def three_path(path):
    current_path = os.path.dirname(__file__)
    # 上一级路径（父级路径）
    parent_path = os.path.dirname(current_path)
    tr_path = os.path.dirname(parent_path)
    join_file_name = tr_path + path
    return join_file_name

# if __name__ == '__main__':
#     version_sql="SELECT VERSION()"  # 查询版本号
#     select_sql="SELECT count(*) FROM baidu_hot"  # 测试数据

    # sql_version=Mysql_link().select_mysql(version_sql)  # 查询版本号
    # res=Mysql_link().select_mysql(select_sql)  # 筛选数据

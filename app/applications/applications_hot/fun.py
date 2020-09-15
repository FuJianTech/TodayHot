#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import datetime
import os
import requests
import json
from collections import OrderedDict
from TodayHot.app.daily_code.fun import Mysql_link
from lxml import etree
from bs4 import BeautifulSoup

class Hot(object):

    def hot_baidu(self):

        def get_html(url, headers):
            r = requests.get(url, headers=headers)
            r.encoding = r.apparent_encoding
            return r.text

        def get_pages(html):
            soup = BeautifulSoup(html, 'html.parser')
            all_topics = soup.find_all('tr')[1:]
            dict_data = {}
            for each_topic in all_topics:
                # topic_link  = each_topic.find('td', class_='')  # 链接
                topic_times = each_topic.find('td', class_='last')  # 搜索指数
                topic_rank = each_topic.find('td', class_='first')  # 排名
                topic_name = each_topic.find('td', class_='keyword')  # 标题目

                if topic_rank is not None and topic_name is not None and topic_times is not None:
                    topic_rank = each_topic.find(
                        'td',
                        class_='first').get_text().replace(
                        ' ',
                        '').replace(
                        '\n',
                        '')
                    topic_name = each_topic.find('td', class_='keyword').get_text() \
                        .replace(' ', '').replace('\n', '') \
                        .replace('search', '')
                    dict_data[topic_rank] = topic_name

            return dict_data

        url = 'http://top.baidu.com/buzz?b=1&fr=20811'
        headers = {'User-Agent': 'Mozilla/5.0'}
        html = get_html(url, headers)
        data = get_pages(html)
        print(113, type(data), data)
        return json.dumps(data)

    def weibo_zhihu(self):
        def get_data(url, num):
            # 解析格式与基础信息
            path = ['//*[@id="TopstoryContent"]/div/div/div[2]/section/div[2]/a',
                    '//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/a']
            web_name = ["知乎热榜",
                        "微博热搜"]

            get_title = ['/h2/text()',
                         '/text()']
            get_link = ['/@href',
                        '/@href']

            # 获取网页
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.8',
                'Cache-Control': 'max-age=0',
                'cookie': '_zap=2a9ae3ab-f2e0-40ff-8a2e-02429c9f0453; d_c0="AGBYvpm7gxGPTiIzHTJtlff00GVsElpFRn0=|1593678215"; _ga=GA1.2.646074918.1593678215; q_c1=a1321aa361ac4df2a0709bb3660b1f60|1596371586000|1596371586000; _gid=GA1.2.1339168512.1596893630; tst=h; tshl=; _xsrf=3woUaVZtwUGqsDKF39WzhwXpU4DZsUV3; SESSIONID=RvdKKA5NNC2mAzAPi145hK2I2IHUIp0Zz16MOt1aWLb; JOID=UloUB0kg0XEVGHmbLiThaxIUcxU-cKQQWFE6rWVskEB9XwHYffEkXU4YeJ0tDY26KUIJ-175v2eF9D1gw2yF8Yk=; osd=W1gdAE8p03gSHnCZJyPnYhAddBM3cq0XXlg4pGJqmUJ0WAfRf_gjW0cacZorBI-zLkQA-Vf-uW6H_Tpmym6M9o8=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1596977420,1596978055,1596978079,1596978130; capsion_ticket="2|1:0|10:1596979172|14:capsion_ticket|44:OWI2NWE3MTVhZDIxNDFiNGI5ZDliZTkzZTE5ZDA1Zjg=|4be161b423d84930ff865a122e22fff3d030d468f49953b4a4dce73318c457e4"; z_c0="2|1:0|10:1596979174|4:z_c0|92:Mi4xNDhPdkFnQUFBQUFBWUZpLW1idURFU1lBQUFCZ0FsVk41a1VkWUFBR0N4dXF4Y2lkdnJDZ2c3bmMtaFhZQ0JjT25B|5020e8ce44cadc7cc35f2ee7b5d1c3f30f85c212d5e4fac081894b11c05110b6"; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1596979708|1596977420; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1596979708',
                'User-Agent': 'Mozilla%d/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36' % random.randint(
                    55, 100),
                'Connection': 'keep-alive',
                'Referer': 'http://www.baidu.com/'
            }
            r = requests.get(url, headers=headers)
            s = etree.HTML(r.text)

            # 获取数据
            titles = s.xpath(path[num] + get_title[num])
            links = s.xpath(path[num] + get_link[num])

            # num==1是微博，由于微博的会出现推荐的话题，这里将其舍去
            if num == 1:
                error = 'javascript:void(0);'
                for j in range(20):
                    if links[j] == error:
                        del links[j]
                        del titles[j]

            # 将前15个结果存到res里
            res = web_name[num] + "\n"
            data_dict = {}
            for i in range(random.randint(10, 15)):
                data_dict[str(i + 1)] = titles[i]
                res = res + str(i + 1) + " " + titles[i]
            return data_dict

        # 爬取url
        url = ['https://www.zhihu.com/hot',
               'https://s.weibo.com/top/summary']
        n = len(url)
        result_list = []
        for i in range(n):
            res = get_data(url[i], i)
            result_list.append(res)
        return result_list

    def key_word(self):

        data_time = datetime.datetime.now().strftime('%Y-%m-%d')
        collect_time = repr(data_time)
        # 测试数据 ，分为关键字和当天文本，返回计数后的数据
        # select_sql_time = f'SELECT content FROM baidu_hot where collect_time = {collect_time}'
        select_sql_keyword = f'SELECT key_word FROM baidu_hot where collect_time = {collect_time}'
        sql_file_name = r'/sql_files/sql_aliyun_2499_hot.ini'

        # 当前路径
        current_path = os.path.dirname(__file__)
        # 上一级路径（父级路径）
        parent_path = os.path.dirname(current_path)
        tr_path = os.path.dirname(parent_path)
        sql_file_name = tr_path + sql_file_name
        print(370, sql_file_name) # 日志查看，勿删

        MQ = Mysql_link(sql_file_name)
        res = list(MQ.select_mysql(select_sql_keyword))


        data_dict = {}
        for key in res:
            key = "".join(key)
            data_dict[key] = data_dict.get(key, 0) + 1

        #  字典根据value排序
        new_dic = OrderedDict(
            sorted(
                data_dict.items(),
                key=lambda kv: kv[1],
                reverse=True))
        last_dic = {item[0]: item[1] for item in new_dic.items()}
        import operator
        last_dic = sorted(last_dic.items(), key=operator.itemgetter(1), reverse=True)[0:9]

        res_dic = {}
        num = 1
        for j in last_dic:
            res_dic[num] = j[0]
            num = num+1
        return res_dic,last_dic


if __name__ == '__main__':
    data  = Hot().key_word()[1]
    print(data)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import bs4
from lxml import etree
from bs4 import BeautifulSoup
from app.daily_code.fun import Mysql_link
from openpyxl import Workbook
import hashlib
import datetime
import os
import requests
import json
import urllib.parse
import time
from collections import OrderedDict

class Hot(object):
    def hot_weibo(self):
        url = "https://s.weibo.com/top/summary"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400"}
        try:
            r = requests.get(url, headers=headers)
        except BaseException:
            print("出现了不可预期的错误")

        hotPattern = re.compile(r'(<tr class="">[\s,\S]*?</tr>)')
        hotList = re.findall(hotPattern, r.text)
        if hotList == []:
            print("匹配模式可能出了问题")
        else:
            # 接下来开始提取热搜数据
            dataList = []
            # print(hotList)
            for hotPoint in hotList:
                data = []
                hotSoup = bs4.BeautifulSoup(hotPoint, 'html.parser')
                # 获取排名
                # print(hotSoup.tr.contents[1])
                rank = hotSoup.tr.contents[1].string
                if rank is None:
                    data.append("速升")
                else:
                    data.append(rank)

                # 获取热搜名称
                # print(hotSoup.tr.contents[3])
                name = hotSoup.tr.contents[3].a.string
                name1 = hotSoup.tr.contents
                data.append(name)
                dataList.append(data)
            dict_data = {}
            # print(dataList)
            for i in dataList:
                # print(i)
                dict_data[i[0]] = i[1]

        return str(dict_data)  # 返回str 用在eval()上

    def hot_baidu(self):

        def get_html(url, headers):
            r = requests.get(url, headers=headers)
            r.encoding = r.apparent_encoding
            return r.text

        def get_pages(html):
            soup = BeautifulSoup(html, 'html.parser')
            all_topics = soup.find_all('tr')[1:]
            dict_data = {}
            data_list = []
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

                    topic_times = each_topic.find(
                        'td',
                        class_='last').get_text().replace(
                        ' ',
                        '').replace(
                        '\n',
                        '')
                    # print('排名：{}，标题：{}，热度：{}'.format(topic_rank,topic_name,topic_times))
                    tplt = "排名：{0:^4}\t标题：{1:{3}^15}\t热度：{2:^8}"
                    tplt = "{0:^4}\t{1:{3}^15}\t热度：{2:^8}"
                    # print(tplt.format(topic_rank, topic_name, topic_times, chr(12288)))

                    # print(topic_rank, topic_name)

                    dict_data[topic_rank] = topic_name
                    # data_list.append(topic_name)  #

            return dict_data

        url = 'http://top.baidu.com/buzz?b=1&fr=20811'
        headers = {'User-Agent': 'Mozilla/5.0'}
        html = get_html(url, headers)
        data = get_pages(html)
        print(113,type(data),data)
        return str(data)

    def hot_zhihu(self):

        url = 'https://s.weibo.com/top/summary?cate=realtimehot'
        r = requests.get(url)
        time.sleep(0.3)
        html = etree.HTML(r.text)
        nodes = html.xpath("//div[@class='data']/table/tbody/tr")
        # print('{:2}   {:7}   {}'.format('序号','搜索次数','热搜内容'))

        dict_result = {}
        for node in nodes[1:]:
            hot_paiming = node.xpath('./td[1]/text()')[0]
            hot_name = node.xpath('./td[2]/a/text()')[0]
            hot_search_nums = node.xpath('./td[2]/span/text()')[0]
            # print('{:2}   {:7}   {}'.format(hot_paiming,hot_search_nums,hot_name))
            dict_result[hot_paiming] = hot_name
        # print(dict_result)
        return dict_result

    def hot_douyin(self):


        '''
        百度热搜，返回数据
        '''
        # 构建请求头
        headers = {
            "Cookie": "install_id=53112482656; ttreq=1$a4ed279b42b9acb3dee9a3a3c2d645ce99ed786f; odin_tt=38d535495242f853ffdf693ae531a152910b1047bbb3ba5c8e2fa7f3cbd7f6a1ec9f6027fc44ea36c4bd45281487d4a7; sid_guard=d074b1c430eef87a3599e20ef34a5555%7C1543976393%7C5184000%7CSun%2C+03-Feb-2019+02%3A19%3A53+GMT; uid_tt=4e0b25bc326fae6b428afc5826243eeb; sid_tt=d074b1c430eef87a3599e20ef34a5555; sessionid=d074b1c430eef87a3599e20ef34a5555",
            "Accept-Encoding": "gzip",
            "X-SS-REQ-TICKET": "1543976807598",
            "X-Tt-Token": "00d074b1c430eef87a3599e20ef34a5555b97ecb95bff1a3d1a81726386a1adf7a91df6c32bfa121fc10400ffede8df72016",
            "sdk-version": "1",
            "X-SS-TC": "0",
            "User-Agent": "com.ss.android.ugc.aweme/350 (Linux; U; Android 8.0.0; zh_CN; MI 5; Build/OPR1.170623.032; Cronet/58.0.2991.0)"
        }

        def getHTML(url):
            '''
            get方式获取html
            :param url:
            :return:
            '''
            rsp = requests.get(url, headers=headers)
            import time
            time.sleep(0.3)
            return rsp.content.decode(rsp.apparent_encoding, 'ignore')

        def postHTML(url):
            '''
            post方式获取html
            :param url:
            :return:
            '''
            rsp = requests.post(url, headers=headers)
            return rsp.content.decode(rsp.apparent_encoding, 'ignore')

        def getVideo(key):
            '''
            获取第一个视频连接地址
            :param key:
            :return:
            '''
            # 编译关键词
            key = urllib.parse.quote(key)
            # 拼接关键词搜索接口url
            url = 'https://api.amemv.com/aweme/v1/general/search/single/?keyword=' + key + \
                '&offset=0&count=10&is_pull_refresh=0&hot_search=0&latitude=30.725991&longitude=103.968091&ts=1543984658&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=350&_rticket=1543984657736&ac=wifi&device_id=60155513971&iid=53112482656&os_version=8.0.0&channel=xiaomi&version_code=350&device_type=MI%205&language=zh&uuid=862258031596696&resolution=1080*1920&openudid=8aa8e21fca47053b&update_version_code=3502&app_name=aweme&version_name=3.5.0&os_api=26&device_brand=Xiaomi&ssmix=a&device_platform=android&dpi=480&aid=1128&as=a1e5055072614ce6a74033&cp=5813c65d2e7d0769e1[eIi&mas=01327dcd31044d72007555ed00c3de0b5dcccc0c2cec866ca6c62c'
            # 获取搜索界面并转化为json对象
            jsonObj = json.loads(postHTML(url))
            # 获取data对应v
            metes = jsonObj['data']
            nums = len(metes)
            uri = ''
            # 多个视频列表捕获第一个视频地址即刻返回视频uri(视频唯一标识)
            for _ in range(nums):
                data = metes[_]['aweme_info']['video']
                if 'download_suffix_logo_addr' in data.keys():
                    uri = data['download_suffix_logo_addr']['uri']
                    break
            # 拼接视频地址
            videoURL = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=' + uri + '&line=0'
            # 返回视频地址
            return videoURL

        def main():
            '''
            入口函数
            :return:
            '''
            ts = str(time.time())
            # 入口url（热门列表url）
            url = 'https://aweme.snssdk.com/aweme/v1/hot/search/list/?detail_list=0&ts=' + ts + '&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=350&_rticket=1543976807872&ac=wifi&device_id=60155513971&iid=53112482656&os_version=8.0.0&channel=xiaomi&version_code=350&device_type=MI%205&language=zh&resolution=1080*1920&openudid=8aa8e21fca47053b&update_version_code=3502&app_name=aweme&version_name=3.5.0&os_api=26&device_brand=Xiaomi&ssmix=a&device_platform=android&dpi=480&aid=1128&as=a1c56320b7f6ccc7874900&cp=3d63c15f7576037de1_uMy&mas=01258b5acd59f6bccb58178086286fdded0c0c9c2cec1cecc6c6c6'
            # 获取热门列表数据
            html = getHTML(url)
            # 转化为json对象
            jsonObj = json.loads(html)
            # 获取每一个热门数据列表
            word_list = jsonObj['data']['word_list']
            index = 1
            # print(word_list)
            dict_data = {}
            # 循环解析每个热门事件
            for li in word_list:
                # try:
                word = li['word']
                # hot_value = li['hot_value']
                hot_index = index
                # videoURL = getVideo(word)
                # print()
                index += 1
                # print(hot_index, word)
                time.sleep(1)
                # print("排名：%d ,关键词: %s ,热度值: %d ,视频下载地址: %s" % (hot_index, word, hot_value, videoURL))
                # except Exception as e:
                #     pass
                # finally:
                #     time.sleep(5)

                dict_data[hot_index] = word

            j = json.dumps(dict_data, ensure_ascii=False)
            return dict_data
            # print(j)
        a = main()
        return a

    def hot_toutiao(self):

        start_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time='
        url = 'https://www.toutiao.com'

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        # 此处cookies可从浏览器中查找，为了避免被头条禁止爬虫
        cookies = {'tt_webid': '6649949084894053895'}

        max_behot_time = '0'  # 链接参数
        title = []  # 存储新闻标题
        source_url = []  # 存储新闻的链接
        s_url = []  # 存储新闻的完整链接
        source = []  # 存储发布新闻的公众号
        media_url = {}  # 存储公众号的完整链接

        def get_as_cp():  # 该函数主要是为了获取as和cp参数，程序参考今日头条中的加密js文件：home_4abea46.js
            zz = {}
            now = round(time.time())
            # print(now) # 获取当前计算机时间
            e = hex(int(now)).upper()[2:]  # hex()转换一个整数对象为16进制的字符串表示
            # print('e:', e)
            a = hashlib.md5()  # hashlib.md5().hexdigest()创建hash对象并返回16进制结果
            # print('a:', a)
            a.update(str(int(now)).encode('utf-8'))
            i = a.hexdigest().upper()
            # print('i:', i)
            if len(e) != 8:
                zz = {'as': '479BB4B7254C150',
                      'cp': '7E0AC8874BB0985'}
                return zz
            n = i[:5]
            a = i[-5:]
            r = ''
            s = ''
            for i in range(5):
                s = s + n[i] + e[i]
            for j in range(5):
                r = r + e[j + 3] + a[j]
            zz = {
                'as': 'A1' + s + e[-3:],
                'cp': e[0:3] + r + 'E1'
            }
            # print('zz:', zz)
            return zz

        def getdata(url, headers, cookies):  # 解析网页函数
            time.sleep(0.3)
            r = requests.get(url, headers=headers, cookies=cookies)
            # print(url)
            data = json.loads(r.text)
            return data

        def savedata(title, s_url, source, media_url):  # 存储数据到文件
            # 存储数据到xlxs文件
            wb = Workbook()
            if not os.path.isdir(os.getcwd() + '/result'):  # 判断文件夹是否存在
                os.makedirs(os.getcwd() + '/result')  # 新建存储文件夹
            filename = os.getcwd() + '/result/result-' + datetime.datetime.now().strftime(
                '%Y-%m-%d-%H-%m') + '.xlsx'  # 新建存储结果的excel文件
            ws = wb.active
            ws.title = 'data'  # 更改工作表的标题
            ws['A1'] = '标题'  # 对表格加入标题
            ws['B1'] = '新闻链接'
            ws['C1'] = '头条号'
            ws['D1'] = '头条号链接'
            for row in range(2, len(title) + 2):  # 将数据写入表格
                _ = ws.cell(column=1, row=row, value=title[row - 2])
                _ = ws.cell(column=2, row=row, value=s_url[row - 2])
                _ = ws.cell(column=3, row=row, value=source[row - 2])
                _ = ws.cell(column=4, row=row,
                            value=media_url[source[row - 2]])

            wb.save(filename=filename)  # 保存文件

        def main(max_behot_time, title, source_url, s_url, source, media_url):  # 主函数
            dict_data = {}
            for i in range(
                    3):  # 此处的数字类似于你刷新新闻的次数，正常情况下刷新一次会出现10条新闻，但夜存在少于10条的情况；所以最后的结果并不一定是10的倍数
                ascp = get_as_cp()  # 获取as和cp参数的函数
                demo = getdata(
                    start_url + max_behot_time + '&max_behot_time_tmp=' + max_behot_time + '&tadrequire=true&as=' +
                    ascp['as'] + '&cp=' + ascp['cp'], headers, cookies)
                # print(demo)
                # time.sleep(1)
                for j in range(len(demo['data'])):
                    # print(demo['data'][j]['title'])
                    if demo['data'][j]['title'] not in title:
                        title.append(demo['data'][j]['title'])  # 获取新闻标题
                        source_url.append(
                            demo['data'][j]['source_url'])  # 获取新闻链接
                        source.append(demo['data'][j]['source'])  # 获取发布新闻的公众号
                    if demo['data'][j]['source'] not in media_url:
                        media_url[demo['data'][j]['source']] = url + \
                            demo['data'][j]['media_url']  # 获取公众号链接
                # print(max_behot_time)
                # 获取下一个链接的max_behot_time参数的值
                max_behot_time = str(demo['next']['max_behot_time'])

                for index in range(len(title)):
                    key = repr(index)
                    value = repr(title[index])
                    dict_data[key] = value.replace('"', '')
            print(dict_data)
            return dict_data
        res = main(max_behot_time, title, source_url, s_url, source, media_url)
        # savedata(title, s_url, source, media_url)
        return res

    def hot_sort(self):

        data_time = datetime.datetime.now().strftime('%Y-%m-%d')
        collect_time = repr(data_time)
        # 测试数据
        select_sql = f'SELECT content FROM baidu_hot where collect_time = {collect_time}'
        # sql_file_name = r'E:\code\xqkj\app\sql_files\sql_aliyun_2499_hot.ini'
        sql_file_name = r'/sql_files/sql_aliyun_2499_hot.ini'

        # 当前路径
        current_path = os.path.dirname(__file__)
        # 上一级路径（父级路径）
        parent_path = os.path.dirname(current_path)
        tr_path = os.path.dirname(parent_path)
        sql_file_name = tr_path + sql_file_name
        print(370,sql_file_name)
        

        MQ = Mysql_link(sql_file_name)
        res = list(MQ.select_mysql(select_sql))
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
        # print(118, last_dic)
        return last_dic
# aa = Hot().hot_zhihu()
# print(aa)

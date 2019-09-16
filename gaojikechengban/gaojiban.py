# #coding=utf8
import requests
import random,string
import random
import json

from collections import Iterable
# url = 'https://tieba.baidu.com/hottopic/browse/topicList'
# headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
# response = requests.get(url)
#
# #拿到http的返回码
# print(response.status_code)
# #拿到text文本返回内容
# print(response.text)
# a_json = response.json()
# print(a_json)
# exp = []
# def get5(getkey, res_dict):
#     global exp
#     if isinstance(res_dict, dict):
#         for k, v in res_dict.items():
#             if k == getkey:
#                 # 把找到数据增加到exp中
#                 exp.append(v)
#                 # 如果每个v只要找一个，可以手动中断
#                 # break
#             get5(getkey, v)
#     elif isinstance(res_dict, list):
#         for ele in res_dict:
#             get5(getkey, ele)
# get5("topic_pic",a_json)
# print(exp)
#
# # url_pic = 'http://imgsrc.baidu.com/forum/pic/item/64380cd7912397dd5cc4f2115682b2b7d0a28762.jpg'
# # res = requests.get(url_pic,headers=
#
#
# for url in exp:
#     pic_name = ''.join(random.sample(string.ascii_lowercase,5)) + '.jpg'
#     with open("pic_name",'wb') as f:          #1、文件名称     2、打开方式：w  wb
#         res = requests.get(url,headers=headers)
#         f.write(res.content)
#         f.close()
#
#
#
# # exp = []
# # def baidu (getkey,a_json):
# #     global exp
# #     if isinstance(a_json,dict):
# #         for k,v in a_json.items():
# #             if k == getkey:
# #                 # print(v)
# #                 exp = exp + v
# #             baidu(getkey,v)
# # baidu("topic_pic",a_json)
# # print(exp)




# 通过headers伪装浏览器，因为有多个地方要使用，所以放在最外面
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}


def get_baidu():
    '''请求百度贴吧的链接，获取到一个json数据'''
    url = 'https://tieba.baidu.com/hottopic/browse/topicList'

    # 模拟浏览器，像百度发起请求，用 r 来装返回结果
    # 注意，这里的headers使用的是全局变量
    r = requests.get(url, headers=headers)
    # 因为这个http的返回结果是json数据类型，所以调用json()方法，将数据转换成字典
    return r.json()


def get_urls(key, res):
    '''从字典中查询出所有的url链接'''
    # 定义(声明)一个空列表用来装链接
    exp = []
    # 函数内部再定义一个递归函数
    def get(getkey, res_dict):
        if isinstance(res_dict, dict):
            for key, value in res_dict.items():
                if key == getkey:
                    print("当前获取到的链接是：%s" % value)
                    exp.append(value)
                    break
                get(getkey, value)
        elif isinstance(res_dict, list):
            for ele in res_dict:
                get(getkey, ele)

    # 执行递归函数
    get(key, res)
    # 把获取到的链接列表返回
    return exp


def download_pic(url_list):
    '''通过链接下载图片，接收一个列表参数'''
    # 遍历这个url列表
    for url in url_list:
        # 生成一个随机的文件名，因为文件名不能重复，不然会覆盖
        pic_name = ''.join(random.sample(string.ascii_lowercase, 5)) + '.jpg'
        with open(pic_name, 'wb') as f:
            # 要下载图片，当然要先发起图片请求咯
            # 注意，这里也会使用全局变量 headers
            r_pic = requests.get(url, headers=headers)
            # 把图片内容写入到文件
            f.write(r_pic.content)
            # 关闭图片文件
            f.close()


if __name__ == '__main__':
    # 在这里来完成所有操作吧
    # 1. 请求百度贴吧，获取到一个字典数据
    res_dict = get_baidu()
    # 2. 利用递归函数，从字典数据中，获取到所有的链接，并组成一个列表
    url_list = get_urls("topic_pic", res_dict)
    print(url_list)
    # 3. 利用for循环把所有的图片都下载下来
    download_pic(url_list)


















































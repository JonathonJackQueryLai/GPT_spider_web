#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 23:26
# @Author  : Jonathon
# @File    : spider.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
import datetime

import requests
import json
import uuid

def gpt_func(string:str):
    # api = "https://gpt.chatapi.art/backend-api/conversation"

    headers1 = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Access-Control-Allow-Origin": "*",
        "Connection": "keep-alive",
        "Content-Length": "83",
        "Content-Type": "application/json",
        "Host": "api.forchange.cn",
        # "Origin": "https://aigcfun.com",
        # "Referer": "https://aigcfun.com/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "x-f-platform": "browser",
        "x-f-uid": f"{str(uuid.uuid4())}"
    }
    api = "https://api.aioschat.com/"
    json_data = json.dumps({'messages': [{'role': "user", 'content': f"{string}"}], 'tokensLength': 1, 'model': "gpt-3.5-turbo"})
    res = requests.post(url=api, data=json_data, headers=headers1,verify=False)
    res = res.json()
    print(res['choices'][0]['text'])

    # print(type(data.text))


if __name__ == '__main__':
    gpt_func('docker面试题')

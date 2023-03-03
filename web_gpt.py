#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 8:04
# @Author  : Jonathon
# @File    : web_gpt.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
from flask import Flask, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', '')
    return f'Hello, {name}!'


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return data


if __name__ == '__main__':
    app.run(debug='True')

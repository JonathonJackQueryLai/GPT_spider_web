#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 0:19
# @Author  : Jonathon
# @File    : openai_demo.py
# @Software: PyCharm
# @ Motto : 客又至，当如何


import openai
openai.api_key = 'xx-xxxxxxxx'

response = openai.Completion.create(
  model='text-davinci-003',
  prompt='主题: 早餐 风\n两句话的恐怖故事:',
  temperature=0.8,
  max_tokens=120,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
)

print(response.choices[0].text)

#!/usr/local/bin/python3
import sys
import requests
import json

url = 'http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh_CN&q='

keyword = sys.argv[1]
result = requests.get(url+keyword)
if result.status_code == 200:
    print(result.json()['sentences'][0]['trans'])
else:
    print('网络错误')

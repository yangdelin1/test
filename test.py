# coding:utf-8
import json

import requests
import urllib3
from operation.user import get_edit_user_info


url = "https://dev-api.banco.com.sg"
url_A = "/ucenter/user/login"
header = {
    "content-type": "application/json; charset=utf-8",
    "Platform": "app.banco.com.sg",
}
data = {
    "account": "vvvwem61@gmail.com",
    "password": "Rt123456!"
}
params = {
    "receiver_cid":"Nm7FHNF483YQyt53RQsGM",
    "category_id":"1",
    "page":"1",
    "limit":"10"
}
urlC = 'https://dev-api.banco.com.sg/ucenter/document/dpo/list'

urlB = url + url_A
print(urlB)
res = requests.post(url=urlB,headers=header,json=data)
print(res.cookies)
data = get_edit_user_info(token = res.cookies)
resA = requests.get(url=urlC,params=params,cookies=res.cookies,headers=header)
print(resA.json())
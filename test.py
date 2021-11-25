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
    "account": "financier_admin@rootant.com",
    "password": "Rt123456!"
}

urlB = url + url_A
print(urlB)
res = requests.post(url=urlB,headers=header,json=data)
print(res.cookies)
data = get_edit_user_info(token = res.cookies)
print(data.response.json().get("message"))
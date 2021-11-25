# coding:utf-8

import pytest
import os
import allure
from api.user import user
from common.logger import run_log as logger
from common.read_data import data

header = data.getJson_value('Headers','/Users/rootant/PycharmProjects/test/data/user.json')
financier_login_data = data.getJson_value('financier_login','/Users/rootant/PycharmProjects/test/data/user.json')
enterprise_login_data = data.getJson_value('enterprise_login','/Users/rootant/PycharmProjects/test/data/user.json')
supplier_login_data = data.getJson_value('supplier_login','/Users/rootant/PycharmProjects/test/data/user.json')

@allure.step("前置步骤==>>管理员用户登录")
def step_login(data):
    logger.info("前置步骤 ==>> 管理员 {} 登录.".format(data))

# @pytest.fixture(scope="session",autouse=True)
# def login_finxture(platform):
#     if platform == 'financier':
#         data = financier_login_data
#         loginInfo = user.login(headers=header,json=data)
#         return loginInfo
#     elif platform == 'enterprise':
#         data = enterprise_login_data
#         loginInfo = user.login(headers=header, json=data)
#         return loginInfo
#     else :
#         data = supplier_login_data
#         loginInfo = user.login(headers=header, json=data)
#         return loginInfo

@pytest.fixture(scope="session",autouse=True)
def financier_login():
    data = financier_login_data
    loginInfo = user.login(headers=header, json=data)
    return loginInfo

# if __name__ == '__main__':
#     cookie = login_finxture(platform="financier")
#     print(cookie.cookies)
#     print(cookie.json().get("data").get("first_name"))
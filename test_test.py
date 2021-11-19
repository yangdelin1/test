# coding:utf-8

import pytest
from common.logger import run_log as logger
import allure


def setup_module():
    logger.info("测试日志模块")
    print("测试日志模块")


def teardown_module():
    logger.info("测试日志模块")
    print("测试日志模块A")

@allure.feature("模型测试模块")
class TestModel:
    def setup_method(self):
        print("测试日志模块")

    def teardown_method(self):
        print('teardownmethod')

    @allure.story("测试test_tt")
    def test_tt(self):
        print('ssssss')

    @allure.story("测试test_mm")
    def test_mm(self):
        print('test mm')

    @allure.story("测试test_ff")
    def test_ff(self):
        print('test ff')
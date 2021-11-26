# coding:utf-8
import allure
from operation.user import get_attachment_id
from common.logger import run_log as logger
import urllib3
urllib3.disable_warnings()

@allure.step("前置登录步骤 ==>>账号登录")
def step_login(admin_user, token):
    logger.info("前置登录步骤 ==>> 管理员 {} 登录 ==>> 返回的 token 为：{}".format(admin_user, token))

@allure.step("签发前置步骤 ==>>获取attachment_id")
def step_get_attachment_id(self,financier_login):
    user_info = financier_login
    result = get_attachment_id()

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对业务流程的测试")
@allure.feature("核心企业签发新票模块")
class TestIssue():
    """签发信票"""

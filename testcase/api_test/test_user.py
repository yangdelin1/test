# coding:utf-8
import pytest
import allure
from operation.user import get_edit_user_info
from common.logger import run_log as logger
import urllib3
urllib3.disable_warnings()

@allure.step("前置登录步骤 ==>>账号登录")
def step_login(admin_user, token):
    logger.info("前置登录步骤 ==>> 管理员 {} 登录 ==>> 返回的 token 为：{}".format(admin_user, token))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户修改个人信息模块")
class TestUpdate():
    """修改用户信息"""

    @allure.story("用例修改用户信息")
    @allure.description("该用例是针对用户修改接口的测试")
    @allure.issue("/ucenter/user/admin/modify/basic", name="修改用户信息")
    @allure.testcase("/ucenter/user/admin/modify/basic", name="修改用户信息")
    def test_update_user(self,financier_login):

        logger.info("*************** 开始执行用例 ***************")
        user_info = financier_login
        admin_user = user_info.json().get("data").get("first_name")
        token = user_info.cookies
        step_login(admin_user, token)
        result = get_edit_user_info(token)
        assert result.response.json().get("message") == "success"
        logger.info("*************** 结束执行用例 ***************")

#
if __name__ == '__main__':
    pytest.main("-q", "-s", "test_user.py")

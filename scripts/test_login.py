import os
import sys

import allure

sys.path.append(os.getcwd())

from base.get_driver import get_driver
from base.read_yaml import ReadYaml


import pytest

from page.page_login import PageLogin


def get_data():
    arrs = []
    for data in ReadYaml("data_login1.yaml").read_yaml().values():
        arrs.append((data.get("username"),data.get("pwd")))
    return arrs


class TestLogin():
    @allure.step("实例化")
    def setup_class(self):
        self.test = PageLogin(get_driver())

    @allure.step("关闭")
    def teardown_class(self):
        self.test.driver.quit()

    @pytest.mark.parametrize("username,pwd",get_data())
    @allure.step("登录步骤")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def testlogin(self,username,pwd):
        allure.attach("描述:","输入用户名")
        self.test.page_input_username(username)
        allure.attach("描述:","输入密码")
        self.test.page_input_pwd(pwd)
        allure.attach("描述:","点击登录")
        self.test.page_click_btn()
        assert 0

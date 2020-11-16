import logging
import time
import pytest
from base.base_analyze import analyze_data
from page.login_page import LoginPage
from utils.driver_utils import DriverUtils

# 登录
class TestLogin:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.login_page = LoginPage(self.driver)
        self.driver.get("http://192.168.1.47:8081/elib/#/login")

    def teardown(self):
        time.sleep(3)
        DriverUtils.quit_driver()

    # 传入json数据
    @pytest.mark.parametrize("params", analyze_data("login_data.json"))
    def test_login(self, params):
        logging.info("login with {}--{}".format(params["username"], params["password"]))
        self.login_page.input_username(params["username"])
        self.login_page.input_password(params["password"])
        self.login_page.click_login_btn()
        self.login_page.click_bm_btn()
        self.login_page.click_wxbm_btn()
        self.login_page.click_bmgl_btn()
        self.login_page.query_btn()

        # 查询成功需要时间, 暂停几秒等待页面
        logging.info("查询中，请稍等...")
        time.sleep(5)
        assert params["msg"] == self.login_page.get_results()

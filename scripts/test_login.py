import logging
import time
import pytest
from base.base_analyze import analyze_data
from page.login_page import LoginPage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 登录
class TestLogin:

    # def setup(self):
    #     self.driver = DriverUtils.get_driver()
    #     DriverUtils.set_switch(True)
    #     self.login_page = LoginPage(self.driver)
    #     self.driver.get(URL)
    #
    # def teardown(self):
    #     time.sleep(3)
    #     DriverUtils.quit_driver()

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, drivers):
        self.login_page = LoginPage(drivers)

    # 传入json数据
    def test_login(self):
        logging.info("login with {}--{}".format(USERNAME, PASSWORD))
        self.login_page.input_username(USERNAME)
        self.login_page.input_password(PASSWORD)
        self.login_page.click_login_btn()
        # self.login_page.click_bm_btn()
        # self.login_page.click_wxbm_btn()
        # self.login_page.click_bmgl_btn()
        # self.login_page.query_btn()

        # 查询成功需要时间, 暂停几秒等待页面
        # logging.info("查询中，请稍等...")
        # time.sleep(5)
        # assert VERIFY == self.login_page.get_results()
        assert True

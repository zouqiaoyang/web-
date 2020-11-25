import time

import pytest

from page.interview.sub2.acceptance_order_manage_page import AcceptanceOrderManagePage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 采访-验收单管理 测试用例
class TestAcceptanceOrderManage:

    # def setup_class(self):
    #     self.driver = DriverUtils.get_driver()
    #     DriverUtils.set_switch(True)
    #     self.page = AcceptanceOrderManagePage(self.driver)
    #     self.driver.get(URL)
    #
    #     self.page.input_username(USERNAME)
    #     self.page.input_password(PASSWORD)
    #     self.page.click_login_btn()
    #
    # def teardown_class(self):
    #     time.sleep(3)
    #     DriverUtils.quit_driver()

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = AcceptanceOrderManagePage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model2()
        self.page.click_menu2()
        self.page.click_sub_menu1()
        self.page.click_sub_menu1_btn()
        assert True

    # @pytest.mark.skip
    def test_details_select(self):
        """ 测试 验收单详情-查询 功能"""
        # 进入征订目录页面
        self.page.click_model2()
        self.page.click_menu2()
        self.page.click_sub_menu1()
        self.page.click_sub_menu1_btn()
        self.page.click_sub_menu2_list()
        self.page.click_sub_menu1_btn()
        assert True





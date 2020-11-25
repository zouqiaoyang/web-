import time

import pytest

from page.interview.sub1.sub_catalog_booking_page import SubCatalogBookingPage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 采访-征订目录预订 测试用例
class TestSubCatalogBooking:

    # def setup_class(self):
    #     self.driver = DriverUtils.get_driver()
    #     DriverUtils.set_switch(True)
    #     self.page = SubCatalogBookingPage(self.driver)
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
        self.page = SubCatalogBookingPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model2()
        self.page.click_menu1()
        self.page.click_sub_menu1()
        self.page.click_sub_menu1_btn()
        assert True

    # @pytest.mark.skip
    def test_details_select(self):
        """ 测试 征订目录详情-查询 功能"""
        # 进入征订目录页面
        self.page.click_model2()
        self.page.click_menu1()
        self.page.click_sub_menu1()
        self.page.click_sub_menu1_btn()
        self.page.click_sub_menu1_list()
        self.page.click_sub_menu1_btn()
        assert True





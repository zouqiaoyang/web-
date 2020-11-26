import time

import pytest

from page.interview.sub1.reservation_order_manage_page import ReservationOrderManagePage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 采访-预订单管理 测试用例
class TestReservationOrderManage:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = ReservationOrderManagePage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model('采访')
        self.page.click_menu('图书预订处理')
        self.page.click_sub_menu(1, '预订单管理')
        self.page.click_sub_menu_btn('查询 ')
        assert self.page.get_sub_menu_alert()

    # @pytest.mark.skip
    def test_details_select(self):
        """ 测试 预订单详情-查询 功能"""
        # 进入征订目录页面
        self.page.click_model('采访')
        self.page.click_menu('图书预订处理')
        self.page.click_sub_menu(1, '预订单管理')
        self.page.click_sub_menu_btn('查询 ')
        self.page.click_sub_menu2_list()
        self.page.click_sub_menu_btn('查询 ')
        assert self.page.get_sub_menu_alert()





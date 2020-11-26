import time

import pytest

from page.interview.sub3.rush_order_page import RushOrderPage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 采访-催缺单 测试用例
class TestRushOrder:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = RushOrderPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model('采访')
        self.page.click_menu('采访报表')
        self.page.click_sub_menu(3, '催缺单')
        self.page.click_sub_menu_btn(' 查询')
        assert self.page.get_sub_menu_alert()
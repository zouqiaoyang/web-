import time
import pytest
from page.circulation.sub1.reservation_management_page import ReservationManagementPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-预约管理 测试用例
class TestReservationManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = ReservationManagementPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("文献流通")
        self.page.click_sub_menu(1, "预约管理")
        self.page.click_sub_menu_btn(" 查询 ")
        assert self.page.get_sub_menu_alert()
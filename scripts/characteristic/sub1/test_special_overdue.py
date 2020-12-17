import time
import pytest
from page.characteristic.sub1.special_overdue_page import SpecialOverduePage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 特色-专项超期管理 测试用例
class TestSpecialOverdue:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = SpecialOverduePage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("特色")
        self.page.click_menu("专项流通")
        self.page.click_sub_menu(1, "专项超期管理")
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.get_sub_menu_alert()
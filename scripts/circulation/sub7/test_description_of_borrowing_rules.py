import time
import pytest
from page.circulation.sub7.description_of_borrowing_rules_page import DescriptionOfBorrowingRulesPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-借阅规则说明 测试用例
class TestHolidaySetting:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = DescriptionOfBorrowingRulesPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("流通参数")
        self.page.click_sub_menu(8, "借阅规则说明")
        self.page.click_sub_menu_btn("查询")
        assert self.page.get_sub_menu_alert()


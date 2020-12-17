import time
import pytest
from page.circulation.sub7.holiday_setting_page import HolidaySettingPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-流通类型 测试用例
class TestHolidaySetting:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = HolidaySettingPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("流通参数")
        self.page.click_sub_menu(8, "假期设定")
        self.page.click_sub_menu_btn("查询")
        assert self.page.get_sub_menu_alert()


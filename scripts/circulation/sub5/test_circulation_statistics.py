import time
import pytest
from page.circulation.sub5.circulation_statistics_page import CirculationStatisticsPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-读者借阅情况 测试用例
class TestCirculationStatistics:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = CirculationStatisticsPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("流通统计")
        self.page.click_sub_menu(5, "流通统计")
        self.page.click_sub_menu_btn("查询 ")
        assert self.page.get_sub_menu_alert()
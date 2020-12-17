import time
import pytest
from page.circulation.sub1.overdue_management_page import OverdueManagementPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-超期管理 测试用例
class TestOverdueManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = OverdueManagementPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("文献流通")
        self.page.click_sub_menu(1, "超期管理")
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.get_sub_menu_alert()
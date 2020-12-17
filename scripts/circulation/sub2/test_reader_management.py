import time
import pytest
from page.circulation.sub2.reader_management_page import ReaderManagementPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-读者管理 测试用例
class TestReaderManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = ReaderManagementPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("读者管理")
        self.page.click_sub_menu(2, "读者管理")
        self.page.click_sub_menu_btn(" 查询 ")
        assert self.page.get_sub_menu_alert()
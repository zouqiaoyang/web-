import time
import pytest
from page.circulation.sub1.borrow_return_management_page import BorrowReturnManagementPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-借还管理 测试用例
class TestBorrowReturnManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = BorrowReturnManagementPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("文献流通")
        self.page.click_sub_menu(1, "借还管理")
        self.page.input_reader_msg("这是一个不存在的测试内容")
        self.page.click_reader_msg_btn()
        assert self.page.get_sub_menu_alert()
import time
import pytest
from page.circulation.sub3.readers_current_borrow_page import ReadersCurrentBorrowPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-读者当前借阅 测试用例
class TestReadersCurrentBorrow:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = ReadersCurrentBorrowPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("流通查询")
        self.page.click_sub_menu(3, "读者当前借阅")
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.get_sub_menu_alert()
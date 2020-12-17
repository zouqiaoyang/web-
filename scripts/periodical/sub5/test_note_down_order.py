import time
import pytest
from page.periodical.sub5.note_down_order_page import NoteDownOrderPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 期刊-记到单 测试用例
class TestNoteDownOrder:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = NoteDownOrderPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("期刊")
        self.page.click_menu("期刊报表")
        self.page.click_sub_menu(5, "记到单")
        self.page.click_sub_menu_btn("查询 ")
        assert self.page.get_sub_menu_alert()
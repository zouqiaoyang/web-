import time
import pytest
from page.periodical.sub4.bookmark_printing_page import BookmarkPrintingPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 期刊-书标打印 测试用例
class TestBookmarkPrinting:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = BookmarkPrintingPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("期刊")
        self.page.click_menu("期刊编目统计")
        self.page.click_sub_menu(4, "书标打印")
        self.page.click_sub_menu_btn("查询")
        assert self.page.get_sub_menu_alert()
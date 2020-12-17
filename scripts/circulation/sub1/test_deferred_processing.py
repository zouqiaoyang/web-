import time
import pytest
from page.circulation.sub1.deferred_processing_page import DeferredProcessingPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-延期处理 测试用例
class TestDeferredProcessing:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = DeferredProcessingPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("文献流通")
        self.page.click_sub_menu(1, "延期处理")
        self.page.click_sub_menu_btn("查询")
        assert self.page.get_sub_menu_alert()
import time
import pytest
from page.periodical.sub2.binding_batch_delivery_page import BindingBatchDeliveryPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 期刊-装订批交送 测试用例
class TestPeriodicalNoted:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = BindingBatchDeliveryPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("期刊")
        self.page.click_menu("期刊记到处理")
        self.page.click_sub_menu(2, "装订批交送")
        self.page.click_sub_menu_btn("查询 ")
        assert self.page.get_sub_menu_alert()
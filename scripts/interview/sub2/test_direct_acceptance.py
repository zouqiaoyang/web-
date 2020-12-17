import time

import pytest

from page.interview.sub2.direct_acceptance_page import DirectAcceptancePage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 采访-直接验收 测试用例
class TestDirectAcceptance:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = DirectAcceptancePage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model('采访')
        self.page.click_menu('图书验收处理')
        self.page.click_sub_menu(2, '直接验收')
        self.page.click_sub_menu_btn(' 查询 ')
        assert self.page.get_sub_menu_alert()
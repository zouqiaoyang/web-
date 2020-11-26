import time

import pytest

from page.interview.sub4.acceptance_classification_page import AcceptanceClassificationPage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 采访-验收分类统计 测试用例
class TestAcceptanceClassification:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = AcceptanceClassificationPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model('采访')
        self.page.click_menu('采访统计')
        self.page.click_sub_menu(4, '验收分类统计')
        self.page.click_sub_menu_btn(' 查询')
        assert self.page.get_sub_menu_alert()
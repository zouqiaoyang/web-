import time
import pytest
from page.characteristic.sub1.special_loan_page import SpecialLoanPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 特色-专项借还管理 测试用例
class TestSpecialLoan:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = SpecialLoanPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("特色")
        self.page.click_menu("专项流通")
        self.page.click_sub_menu(1, "专项借还管理")
        self.page.input_reader_msg("这是一个不存在的测试内容")
        self.page.click_reader_msg_btn()
        assert self.page.get_sub_menu_alert()
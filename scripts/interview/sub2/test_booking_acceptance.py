import time

import pytest

from page.interview.sub2.booking_acceptance_page import BookingAcceptancePage
from utils.driver_utils import DriverUtils
from config.base_config import *

# 采访-预订验收 测试用例
class TestBookingAcceptance:

    # def setup_class(self):
    #     self.driver = DriverUtils.get_driver()
    #     DriverUtils.set_switch(True)
    #     self.page = BookingAcceptancePage(self.driver)
    #     self.driver.get(URL)
    #
    #     self.page.input_username(USERNAME)
    #     self.page.input_password(PASSWORD)
    #     self.page.click_login_btn()
    #
    # def teardown_class(self):
    #     time.sleep(3)
    #     DriverUtils.quit_driver()

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = BookingAcceptancePage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model2()
        self.page.click_menu2()
        self.page.click_sub_menu2()
        self.page.click_sub_menu2_btn()
        assert True
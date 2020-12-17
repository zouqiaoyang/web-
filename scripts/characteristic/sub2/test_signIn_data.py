import time
import pytest
from page.characteristic.sub2.signIn_data_page import SignInDataPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 特色-签到数据 测试用例
class TestSignInData:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = SignInDataPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("特色")
        self.page.click_menu("义工管理")
        self.page.click_sub_menu(2, "签到数据")
        self.page.click_sub_menu_btn("查询")
        assert self.page.get_sub_menu_alert()
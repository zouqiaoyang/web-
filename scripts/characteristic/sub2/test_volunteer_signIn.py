import time
import pytest
from page.characteristic.sub2.volunteer_signIn_page import VolunteerSignInPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 特色-义工签到 测试用例
class TestVolunteerSignIn:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = VolunteerSignInPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(1)

    # @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("特色")
        self.page.click_menu("义工管理")
        self.page.click_sub_menu(2, "义工签到")
        self.page.input_reader_msg("这是一个不存在的测试内容")
        self.page.click_reader_msg_btn()
        assert self.page.get_sub_menu_alert()
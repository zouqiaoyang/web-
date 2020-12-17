import time
import pytest
from page.circulation.sub5.types_of_readers_page import TypesOfReadersPage
from utils.driver_utils import DriverUtils
from config.base_config import *


# 流通-读者类型借还统计 测试用例
class TestTypesOfReaders:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = TypesOfReadersPage(drivers)

    def teardown_class(self):
        DriverUtils.back_ops()
        time.sleep(3)

    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_model("流通")
        self.page.click_menu("流通统计")
        self.page.click_sub_menu(5, "读者类型借还统计")
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.get_sub_menu_alert()
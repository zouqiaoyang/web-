# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

# 特色-义工签到
class VolunteerSignInPage(BasePage):

    reader_msg_input = By.XPATH, "//div[@class='readerTop']/div[1]/div/input"   # 读者信息-读者证号输入框
    reader_msg_btn = By.XPATH, "//div[@class='readerTop']/div[1]/button"     # 读者信息-确定按钮

    def input_reader_msg(self, content):
        self.input(self.reader_msg_input, content)

    def click_reader_msg_btn(self):
        self.click(self.reader_msg_btn)

    def get_sub_menu_alert(self):
        element = self.find_el((By.XPATH, "//p[contains(text(), '签到地点不能为空')]"))
        return element.is_enabled()     # 判断元素是否可用，返回布尔值
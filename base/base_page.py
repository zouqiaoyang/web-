# -*- coding:utf-8 -*-
from base.base_action import BaseAction
from selenium.webdriver.common.by import By

class BasePage(BaseAction):

    def click_model(self, name):
        value = "//*[@alt='{0}']".format(name)
        self.click((By.XPATH, value))

    def click_menu(self, name):
        value = "//span[contains(text(), '{0}')]".format(name)
        self.click((By.XPATH, value))

    def click_sub_menu(self, num, name):
        value = "//li[{0}]/ul/li[contains(text(), '{1}')]".format(num, name)
        self.click((By.XPATH, value))

    def click_sub_menu_btn(self, name):
        value = "//span[contains(text(), '{0}')]".format(name)
        self.click((By.XPATH, value))

    # 如果len(element)长度为0，则错误提示框不存在；存在则测试不通过
    def get_sub_menu_alert(self):
        element = self.find_el((By.XPATH, "//i[@class='el-message__icon el-icon-error']"))
        return True if len(element) == 0 else False
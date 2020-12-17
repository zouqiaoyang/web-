# -*- coding:utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
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
        value = "//li[{0}]/ul/li[text()='{1}']".format(num, name)
        # value = "//li[{0}]/ul/li[contains(text(), '{1}')]".format(num, name)
        self.click((By.XPATH, value))

    def click_sub_menu_btn(self, name):
        """
        比如查找 查询 按钮时，如果 subMenu 有包含查询这个字段就会定位不到，必须在span加个button辅助定位
        :param name: 按钮文本
        :return: element
        """
        value = "//button/span[contains(text(), '{0}')]".format(name)
        self.click((By.XPATH, value))

    def get_sub_menu_alert(self):
        """ 判断是否有提示框
        没有默认为查找成功，有提示框判断提示框的class元素中是否含有el-message--error，含有则为False，不含有则不是错误提示框为成功
        str.find()：找不到返回-1，找到返回下标
        """
        element = self.find_el((By.XPATH, "//div[@role='alert']"))
        if element is None or str(element.get_attribute('class')).find("el-message--error") == "-1":
            return True
        return False
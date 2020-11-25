# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import logging
import time

# 采访-直接预订

class DirectBookingPage(BaseAction):

    model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    menu1 = By.XPATH, "//span[contains(text(), '图书预订处理')]"  # 图书预订处理 按钮
    sub_menu3 = By.XPATH, "//li[contains(text(), '直接预订')]"      # 直接预订按钮
    sub_menu3_btn = By.XPATH, "//span[contains(text(), ' 查询 ')]"  # 直接预订-查询 按钮

    def click_model2(self):
        self.click(self.model2)

    def click_menu1(self):
        self.click(self.menu1)

    def click_sub_menu3(self):
        self.click(self.sub_menu3)

    def click_sub_menu3_btn(self):
        self.click(self.sub_menu3_btn)
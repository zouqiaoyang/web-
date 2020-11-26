# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

# 采访-预订验收

class BookingAcceptancePage(BasePage):
    pass
    # model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    # menu2 = By.XPATH, "//span[contains(text(), '图书验收处理')]"  # 图书验收处理 按钮
    # sub_menu2 = By.XPATH, "//li[contains(text(), '预订验收')]"      # 预订验收按钮
    # sub_menu2_btn = By.XPATH, "//span[contains(text(), ' 查询 ')]"  # 预订验收-查询 按钮

    # def click_model2(self):
    #     self.click(self.model2)
    #
    # def click_menu2(self):
    #     self.click(self.menu2)
    #
    # def click_sub_menu2(self):
    #     self.click(self.sub_menu2)
    #
    # def click_sub_menu2_btn(self):
    #     self.click(self.sub_menu2_btn)
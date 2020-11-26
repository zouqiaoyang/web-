# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

# 采访-验收单
class AcceptanceOrderPage(BasePage):
    pass
    # model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    # menu3 = By.XPATH, "//span[contains(text(), '采访报表')]"  # 采访报表 按钮
    # sub_menu3 = By.XPATH, "//li[3]/ul/li[contains(text(), '验收单')]"      # 验收单按钮
    # sub_menu3_btn = By.XPATH, "//button/span[contains(text(), '查询')]"  # 验收单-查询 按钮

    # def click_model2(self):
    #     self.click(self.model2)
    #
    # def click_menu3(self):
    #     self.click(self.menu3)
    #
    # def click_sub_menu3(self):
    #     self.click(self.sub_menu3)
    #
    # def click_sub_menu3_btn(self):
    #     self.click(self.sub_menu3_btn)
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

# 采访-货币汇率
class CurrencyPage(BasePage):
    pass
    # model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    # menu5 = By.XPATH, "//span[contains(text(), '采编参数')]"  # 采编参数 按钮
    # sub_menu5 = By.XPATH, "//li[5]/ul/li[contains(text(), '货币汇率')]"      # 货币汇率按钮
    # sub_menu5_btn = By.XPATH, "//button/span[contains(text(), ' 查询')]"  # 货币汇率-查询 按钮

    # def click_model2(self):
    #     self.click(self.model2)
    #
    # def click_menu5(self):
    #     self.click(self.menu5)
    #
    # def click_sub_menu5(self):
    #     self.click(self.sub_menu5)
    #
    # def click_sub_menu5_btn(self):
    #     self.click(self.sub_menu5_btn)
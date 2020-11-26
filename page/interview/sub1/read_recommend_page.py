# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

# 采访-读者荐购
class ReadRecommendPage(BasePage):
    pass

    # model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    # menu1 = By.XPATH, "//span[contains(text(), '图书预订处理')]"  # 图书预订处理 按钮
    # sub_menu4 = By.XPATH, "//li[contains(text(), '读者荐购')]"      # 预订单管理按钮
    # sub_menu4_btn = By.XPATH, "//span[contains(text(), ' 查询')]"  # 预订单管理-查询 按钮
    #
    # def click_model2(self):
    #     self.click(self.model2)
    #
    # def click_menu1(self):
    #     self.click(self.menu1)
    #
    # def click_sub_menu4(self):
    #     self.click(self.sub_menu4)
    #
    # def click_sub_menu4_btn(self):
    #     self.click(self.sub_menu4_btn)
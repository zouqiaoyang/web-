# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

# 采访-验收单管理

class AcceptanceOrderManagePage(BasePage):

    # model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    # menu2 = By.XPATH, "//span[contains(text(), '图书验收处理')]"  # 图书验收处理 按钮
    # sub_menu1 = By.XPATH, "//li[contains(text(), '验收单管理')]"      # 验收单管理按钮
    # sub_menu1_btn = By.XPATH, "//span[contains(text(), ' 查询')]"  # 验收单管理-查询 按钮
    # 验收单名称，点击跳转验收单详情
    sub_menu_list = By.XPATH, "//*[@class='content__table']/div/div[3]/table/tbody/tr[1]/td[3]/div/span"

    # def click_model2(self):
    #     self.click(self.model2)
    #
    # def click_menu2(self):
    #     self.click(self.menu2)
    #
    # def click_sub_menu1(self):
    #     self.click(self.sub_menu1)
    #
    # def click_sub_menu1_btn(self):
    #     self.click(self.sub_menu1_btn)

    def click_sub_menu_list(self):
        self.click(self.sub_menu_list)
        time.sleep(3)
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

# 采访-征订目录预订

class SubCatalogBookingPage(BasePage):

    # model2 = By.XPATH, "//*[@alt='采访']"              # 采访 按钮
    # menu1 = By.XPATH, "//span[contains(text(), '图书预订处理')]"    # 图书预订处理 按钮
    # sub_menu1 = By.XPATH, "//li[contains(text(), '征订目录预订')]"      # 征订目录预订 按钮
    # sub_menu1_btn = By.XPATH, "//span[contains(text(), ' 查询')]"      # 征订目录预订-查询 按钮
    sub_menu_list = By.XPATH, "//*[@class='content__table']/div/div[3]/table/tbody/tr[1]/td[3]/div/span"

    # def click_model2(self):
    #     self.click(self.model2)
    #
    # def click_menu1(self):
    #     self.click(self.menu1)
    #
    # def click_sub_menu1(self):
    #     self.click(self.sub_menu1)
    #
    # def click_sub_menu1_btn(self):
    #     self.click(self.sub_menu1_btn)

    def click_sub_menu_list(self):
        self.click(self.sub_menu_list)
        time.sleep(3)
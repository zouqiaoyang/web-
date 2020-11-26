# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage

# 采访-直接预订

class DirectBookingPage(BasePage):
    pass

    # model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    # menu1 = By.XPATH, "//span[contains(text(), '图书预订处理')]"  # 图书预订处理 按钮
    # sub_menu3 = By.XPATH, "//li[contains(text(), '直接预订')]"      # 直接预订按钮
    # sub_menu3_btn = By.XPATH, "//span[contains(text(), ' 查询 ')]"  # 直接预订-查询 按钮
    # sub_menu3_alert = By.XPATH, "//i[@class='el-message__icon el-icon-error']"  # 获取提示框

    # def click_model2(self):
    #     self.click(self.model2)
    #
    # def click_menu1(self):
    #     self.click(self.menu1)
    #
    # def click_sub_menu3(self):
    #     self.click(self.sub_menu3)
    #
    # def click_sub_menu3_btn(self):
    #     self.click(self.sub_menu3_btn)
    #
    # # 如果len(element)长度为0，则错误提示框不存在；存在则测试不通过
    # def get_sub_menu3_alert(self):
    #     element = self.find_el(self.sub_menu3_alert)
    #     return True if len(element) == 0 else False
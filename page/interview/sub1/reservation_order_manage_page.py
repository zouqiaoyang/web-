# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import time

# 采访-预订单管理

class ReservationOrderManagePage(BaseAction):

    username_input = By.XPATH, "//*[@placeholder='请输入用户名']"  # 用户名 输入框
    password_input = By.XPATH, "//*[@placeholder='请输入密码']"  # 密码 输入框
    login_btn = By.XPATH, "//*[@type='button']"  # 登录 按钮

    model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    menu1 = By.XPATH, "//span[contains(text(), '图书预订处理')]"  # 图书预订处理 按钮
    sub_menu2 = By.XPATH, "//li[contains(text(), '预订单管理')]"      # 预订单管理按钮
    sub_menu2_btn = By.XPATH, "//span[contains(text(), '查询 ')]"  # 预订单管理-查询 按钮
    # 预订单名称，点击跳转预订单详情
    sub_menu2_list = By.XPATH, "//*[@class='content__table']/div/div[3]/table/tbody/tr[1]/td[3]/div/span"


    def input_username(self, content):
        self.input(self.username_input, content)

    def input_password(self, content):
        self.input(self.password_input, content)

    def click_login_btn(self):
        self.click(self.login_btn)

    def click_model2(self):
        self.click(self.model2)

    def click_menu1(self):
        self.click(self.menu1)

    def click_sub_menu2(self):
        self.click(self.sub_menu2)

    def click_sub_menu2_btn(self):
        self.click(self.sub_menu2_btn)

    def click_sub_menu2_list(self):
        self.click(self.sub_menu2_list)
        time.sleep(3)
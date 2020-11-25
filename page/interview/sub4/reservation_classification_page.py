# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import time

# 采访-预订分类统计
class ReservationClassificationPage(BaseAction):

    username_input = By.XPATH, "//*[@placeholder='请输入用户名']"  # 用户名 输入框
    password_input = By.XPATH, "//*[@placeholder='请输入密码']"  # 密码 输入框
    login_btn = By.XPATH, "//*[@type='button']"  # 登录 按钮

    model2 = By.XPATH, "//*[@alt='采访']"  # 采访 按钮
    menu4 = By.XPATH, "//span[contains(text(), '采访统计')]"  # 采访统计 按钮
    sub_menu3 = By.XPATH, "//li[4]/ul/li[contains(text(), '预订分类统计')]"      # 预订分类统计按钮
    sub_menu3_btn = By.XPATH, "//button/span[contains(text(), ' 查询')]"  # 预订分类统计-查询 按钮

    def input_username(self, content):
        self.input(self.username_input, content)

    def input_password(self, content):
        self.input(self.password_input, content)

    def click_login_btn(self):
        self.click(self.login_btn)

    def click_model2(self):
        self.click(self.model2)

    def click_menu4(self):
        self.click(self.menu4)

    def click_sub_menu3(self):
        self.click(self.sub_menu3)

    def click_sub_menu3_btn(self):
        self.click(self.sub_menu3_btn)
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import time

# 采访-征订目录预订

class SubCatalogBookingPage(BaseAction):

    username_input = By.XPATH, "//*[@placeholder='请输入用户名']"  # 用户名 输入框
    password_input = By.XPATH, "//*[@placeholder='请输入密码']"    # 密码 输入框
    login_btn = By.XPATH, "//*[@type='button']"                  # 登录 按钮
    # login_name = By.XPATH, "//*[@class='user']/span/button/span/span"  # 登录-管理员名称

    model2 = By.XPATH, "//*[@alt='采访']"              # 采访 按钮
    menu1 = By.XPATH, "//span[contains(text(), '图书预订处理')]"    # 图书预订处理 按钮
    sub_menu1 = By.XPATH, "//li[contains(text(), '征订目录预订')]"      # 征订目录预订 按钮
    sub_menu1_btn = By.XPATH, "//span[contains(text(), ' 查询')]"      # 征订目录预订-查询 按钮
    # sub_menu1_msg = By.XPATH, "//*[span='暂无数据']"    # 征订目录预订-查询-暂无数据 文本
    # sub_menu1_opt = By.XPATH, "//*[@class='content__table']/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div"   # 操作按钮
    # 征订目录名称，点击跳转征订目录详情
    sub_menu1_list = By.XPATH, "//*[@class='content__table']/div/div[3]/table/tbody/tr[1]/td[3]/div/span"

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

    def click_sub_menu1(self):
        self.click(self.sub_menu1)

    def click_sub_menu1_btn(self):
        self.click(self.sub_menu1_btn)

    # def select_sub_menu1_msg(self):
    #     return self.text(self.sub_menu1_msg)

    # def select_name_msg(self):
    #     return self.text(self.login_name)

    # def click_sub_menu1_opt(self):
    #     self.click(self.sub_menu1_opt)
    #     time.sleep(3)

    def click_sub_menu1_list(self):
        self.click(self.sub_menu1_list)
        time.sleep(3)
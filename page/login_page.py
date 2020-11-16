from selenium.webdriver.common.by import By
from base.base_action import BaseAction

# 编目管理查询
class LoginPage(BaseAction):

    # 用户名 输入框
    username_input = By.XPATH, "//*[@placeholder='请输入用户名']"
    # 密码 输入框
    password_input = By.XPATH, "//*[@placeholder='请输入密码']"
    # 登录 按钮
    login_btn = By.XPATH, "//*[@type='button']"
    # 编目 按钮
    bm_btn = By.XPATH, "//*[@alt='编目']"
    # 文献编目 按钮
    wxbm_btn = By.XPATH, "//*[span='文献编目']"
    # 编目管理 按钮
    bmgl_btn = By.XPATH, "//*[li='编目管理']"
    # 查询 按钮
    query_btn = By.XPATH, "//*[span=' 查询 ']"
    # 查询结果
    query_results = By.XPATH, "//*[div='1']"

    # 输入用户名
    def input_username(self, content):
        return self.input(self.username_input, content)

    # 输入密码
    def input_password(self, content):
        return self.input(self.password_input, content)

    # 点击登录按钮
    def click_login_btn(self):
        return self.click(self.login_btn)

    # 点击编目按钮
    def click_bm_btn(self):
        return self.click(self.bm_btn)

    # 点击文献编目按钮
    def click_wxbm_btn(self):
        return self.click(self.wxbm_btn)

    # 点击编目管理按钮
    def click_bmgl_btn(self):
        return self.click(self.bmgl_btn)

    # 点击查询按钮
    def click_query_btn(self):
        return self.click(self.query_btn)

    # 获取查询结果
    def get_results(self):
        return self.find_el(self.query_results)
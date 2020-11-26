from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

# 基类
class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

    # 查找单个元素
    def find_el(self, feature):
        # return self.driver.find_element(*feature)
        by, value = feature
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value)))
        except (NoSuchElementException, TimeoutException):
            logging.error("No Such Element："+value)

    # 查找多个元素
    def find_els(self, feature):
        # return self.driver.find_elements(*feature)
        by, value = feature
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((by, value)))
        except (NoSuchElementException, TimeoutException):
            logging.error("No Such Element：" + value)

    # 点击
    def click(self, feature):
        return self.find_el(feature).click()

    # 输入
    def input(self, feature, content):
        return self.find_el(feature).send_keys(content)

    # 清除
    def clear(self, feature):
        return self.find_el(feature).clear()

    # 切换
    def switch_to(self, frame_feature):
        return self.driver.switch_to.frame(self.find_el(frame_feature))

    # 切换到默认
    def switch_to_default(self):
        return self.driver.switch_to.default_content()

    # 切换窗口
    def switch_window(self):
        handlers = self.driver.window_handles
        return self.driver.switch_to.window(handlers[-1])

    # 获取页面源代码
    def get_source(self):
        return self.driver.page_source

    # 获取当前组件文本
    def text(self, feature):
        return self.find_el(feature).text

    # 刷新页面
    def refresh(self):
        self.driver.refresh()
        # self.driver.implicitly_wait(30)

    # 浏览器后退
    def back(self):
        self.driver.back()
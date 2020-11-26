import logging
from config.base_config import *
from selenium import webdriver

# 工具类
class DriverUtils:
    __driver = None
    __switch = False

    # 获取浏览器驱动
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            logging.info("creat chrome driver")
            cls.__driver = webdriver.Chrome(options=CHROME_OPTIONS)
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(5)
        else:
            logging.info("use existed chrome driver")
        return cls.__driver

    # 关闭浏览器驱动
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            logging.info("quit chrome driver")
            cls.__driver.quit()
            cls.__driver = None
        else:
            logging.info("chrome driver is still alive")

    @classmethod
    def set_switch(cls, switch):
        cls.__switch = switch

    @classmethod
    def back_ops(cls):
        # time.sleep(2)
        cls.__driver.find_element_by_xpath("//div[@class='el-scrollbar__view']/span[1]").click()
        cls.__driver.refresh()
        pass
# 基类
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 查找单个元素
    def find_el(self, feature):
        return self.driver.find_element(*feature)

    # 查找多个元素
    def find_els(self, feature):
        return self.driver.find_elements(*feature)

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
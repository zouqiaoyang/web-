# -*- coding:utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 业务系统地址
URL = 'http://192.168.1.35:8080/elib/#/login'
# URL = 'https://yun.library3.cn/elib/#/login'

# Chrome 设置
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument('disable-infobars')
# CHROME_OPTIONS.add_argument("headless")
CHROME_OPTIONS.add_argument('profile.managed_default_content_settings.images')
CHROME_OPTIONS.add_argument('lang=zh_CN.UTF-8')
CHROME_OPTIONS.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"')

# 测试账号
USERNAME = 'zll'
PASSWORD = 'Td123456'
VERIFY = '钟礼隆'
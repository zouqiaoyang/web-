# -*- coding:utf-8 -*-
import pytest
import time
from utils.driver_utils import DriverUtils
from config.base_config import *

driver = None

@pytest.fixture(scope='session', autouse=True)
def drivers():
    global driver
    driver = DriverUtils.get_driver()
    DriverUtils.set_switch(True)
    driver.get(URL)
    yield driver
    time.sleep(3)
    DriverUtils.quit_driver()
    return driver
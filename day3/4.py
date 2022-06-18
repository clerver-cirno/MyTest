#不可以运行

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\注册A.html")

ele=driver.find_element_by_css_selector("select")

sel=Select(ele)

sel.select_by_index(1)

driver.quit()

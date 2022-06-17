import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\注册A.html")

ele=driver.find_element_by_css_selector("input[name=userA]")

action=ActionChains(driver)

action.context_click(ele)
action.perform()

time.sleep(3)

driver.quit()
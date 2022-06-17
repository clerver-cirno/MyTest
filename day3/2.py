import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\drag.html")

ele1=driver.find_element_by_css_selector("body div[id=div1]")
ele2=driver.find_element_by_css_selector("body div[id=div2]")

action=ActionChains(driver)

action.drag_and_drop(ele1, ele2)
action.perform()

time.sleep(3)

driver.quit()

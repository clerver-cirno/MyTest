import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\注册A.html")

user=driver.find_element_by_css_selector("input[name=userA]")

user.send_keys("admin1")
time.sleep(2)

user.send_keys(Keys.BACK_SPACE)
time.sleep(2)

user.send_keys(Keys.CONTROL, 'A')
time.sleep(2)

user.send_keys(Keys.CONTROL,'C')
time.sleep(2)

driver.find_element_by_css_selector("input[name=passwordA]").send_keys(Keys.CONTROL,"V")
time.sleep(2)

driver.quit()
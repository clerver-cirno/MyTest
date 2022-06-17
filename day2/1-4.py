import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\注册A.html")

driver.set_window_size(300,300)
time.sleep(3)
driver.set_window_position(300,300)
time.sleep(3)
driver.quit()
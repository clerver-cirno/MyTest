import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\注册A.html")

driver.find_element_by_css_selector("p input").send_keys("admin")

time.sleep(3)

driver.quit()
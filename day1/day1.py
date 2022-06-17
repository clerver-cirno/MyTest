from selenium import webdriver
import time
driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\注册A.html")

driver.find_element_by_name("passwordA").send_keys("123456")

time.sleep(3)

driver.find_element_by_xpath("//form/p/button").click()

driver.quit()
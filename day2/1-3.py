import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("D:\作业\软件质量保证与测试实习\Web自动化测试\page\注册A.html")

driver.find_element_by_css_selector("[name=userA]").send_keys("admin")

driver.find_element_by_css_selector("input[name=passwordA]").send_keys("123456")

driver.find_element_by_css_selector("[name=telA]").send_keys("18611111111")

driver.find_element_by_css_selector("[name=emailA]").send_keys("123@qq.com")

time.sleep(3)

driver.find_element_by_css_selector("[name=telA]").clear()

driver.find_element_by_css_selector("[name=telA]").send_keys("18600000000")

time.sleep(3)

driver.find_element_by_css_selector("button").click()

time.sleep(3)

driver.quit()
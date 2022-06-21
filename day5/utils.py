import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def get_mobile():
    mobiles = ['140', '141', '142', '143', '144']
    number  = str(int(time.time()))[2:]
    mobile  = random.choice(mobiles)+number
    return mobile

def get_element(driver, position):
    wait = WebDriverWait(driver, 10, 1)
    element = wait.until(lambda x: x.find_element(*position))
    return element
def auto_login(driver):
    # 进入首页，点击登录按钮
    go_login = (By.CSS_SELECTOR, ".red")
    get_element(driver, go_login).click()
    # 输入用户名
    ele_moble = By.ID, "username"
    get_element(driver, ele_moble).send_keys("17628029450")
    # 输入密码
    ele_pw = By.ID, 'password'
    get_element(driver, ele_pw).send_keys("12345678")
    # 输入验证码
    ele_code = By.ID, 'verify_code'
    get_element(driver, ele_code).send_keys("8888")
    # 点击登录
    ele_login = By.CSS_SELECTOR, '.J-login-submit'
    get_element(driver, ele_login).click()
    time.sleep(2)
    # 回到首页
    driver.get("http://www.localhost.net")

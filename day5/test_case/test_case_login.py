import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from parameterized import parameterized

from day5.utils import get_element



class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.localhost.net")
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("http://www.localhost.net")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    case_data = [('17628029450', '12345678', '88888', '验证码错误', False),
                 ('', '12345678', '8888', '用户名不能为空', False),
                 ('17628029450', '', '8888', '密码不能为空', False),
                 ('17628029450', '12345678', '', '验证码不能为空', False),
                 ('17628029450', '123456787', '8888', '密码错误', False),
                 ('17628029450', '12345678', '8888', '我的账户', True)]

    @parameterized.expand(case_data)
    def test_login(self, mobile, password, code, expect, is_success):
        # 进入首页，点击登录按钮
        go_login = (By.CSS_SELECTOR, ".red")
        get_element(self.driver, go_login).click()
        # 输入用户名
        ele_moble = By.ID, "username"
        get_element(self.driver, ele_moble).send_keys(mobile)
        # 输入密码
        ele_pw = By.ID, 'password'
        get_element(self.driver, ele_pw).send_keys(password)
        # 输入验证码
        ele_code = By.ID, 'verify_code'
        get_element(self.driver, ele_code).send_keys(code)
        # 点击登录
        ele_login = By.CSS_SELECTOR, '.J-login-submit'
        get_element(self.driver, ele_login).click()
        time.sleep(2)
        if is_success:
            msg = self.driver.title
        else:
            msg = get_element(self.driver, (By.CSS_SELECTOR, ".layui-layer-content")).text
        self.assertIn(expect, msg)

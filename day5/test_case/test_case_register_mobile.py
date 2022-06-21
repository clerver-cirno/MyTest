import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from parameterized import parameterized

from day5.utils import get_element, get_mobile


class TestRegisterByMobile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.localhost.net")
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("http://www.localhost.net")

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    expect = "首页-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
    case_data = [(get_mobile() + '1', '8888', '12345678', '12345678', False),  # 手机号不为11位
                 ('13757573a38', '8888', '12345678', '12345678', False),  # 手机号不是纯数字
                 ('', '8888', '12345678', '12345678', False),  # 手机号为空
                 (get_mobile(), '', '12345678', '12345678', False),  # 验证码为空
                 (get_mobile(), '88888', '12345678', '12345678', False),  # 验证码不正确
                 (get_mobile(), '8888', '12345678', '111111111', False),  # 密码和密码2不一样
                 (get_mobile(), '8888', '12345678', '', False),  # 密码2为空
                 (get_mobile(), '8888', '', '', False),  # 密码全为空
                 (get_mobile(), '8888', '12345', '12345', False),  # 密码小于6位
                 (get_mobile(), '8888', '12345678123456781', '12345678123456781', False),  # 密码大于16位
                 (get_mobile(), '8888', '12345678', '12345678', True)
                 ]

    @parameterized.expand(case_data)
    def test_register(self, mobile, code, password, password2, is_success):
        # 进入首页，点击注册按钮
        go_login = (By.XPATH, "*//a[@href='/Home/user/reg.html']")
        get_element(self.driver, go_login).click()
        # 输入电话
        ele_moble = By.ID, "username"
        get_element(self.driver, ele_moble).send_keys(mobile)
        # 输入验证码
        ele_code = By.NAME, 'verify_code'
        get_element(self.driver, ele_code).send_keys(code)
        # 输入密码
        ele_pw = By.ID, 'password'
        get_element(self.driver, ele_pw).send_keys(password)
        # 确认密码
        ele_pw2 = By.ID, 'password2'
        get_element(self.driver, ele_pw2).send_keys(password2)
        # 点击注册
        ele_reg = By.CSS_SELECTOR, '.regbtn'
        get_element(self.driver, ele_reg).click()
        time.sleep(5)
        msg = self.driver.title
        if is_success:
            self.assertIn(self.expect, msg)
        else:
            self.assertNotIn(self.expect, msg)

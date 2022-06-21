import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from parameterized import parameterized
from selenium.webdriver.support.wait import WebDriverWait

from day5.utils import get_element, get_mobile, auto_login


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.localhost.net")
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("http://www.localhost.net")
        auto_login(self.driver)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_order(self):

        # 搜索框输入iPhone 6s
        ele_input = By.CSS_SELECTOR, "input[name=q]"
        get_element(self.driver, ele_input).send_keys("iphone 6s")
        # 点击搜索按钮
        ele_search = By.CSS_SELECTOR, 'button'
        get_element(self.driver, ele_search).click()
        # 打开详情页
        ele_page=By.CSS_SELECTOR,"a img[class=lazy-list]"
        get_element(self.driver,ele_page).click()
        time.sleep(2)
        #点击立即购买按钮
        ele_pay=By.CSS_SELECTOR,'a[class=paybybill]'
        get_element(self.driver,ele_pay).click()
        time.sleep(2)
        #点击提交订单按钮
        ele_sub_orders=By.CSS_SELECTOR,'a[onclick="submit_order();"]'
        get_element(self.driver,ele_sub_orders).click()
        time.sleep(5)
        #选择货到付款按钮
        ele_pay_radio=By.CSS_SELECTOR,'input[value="pay_code=cod"]'
        get_element(self.driver,ele_pay_radio).click()
        #点击确认支付按钮
        ele_conf_pay=By.CSS_SELECTOR,'''a[onclick="$('#cart4_form').submit();"]'''
        get_element(self.driver,ele_conf_pay).click()
        time.sleep(2)
        expect='支付成功-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城'
        msg=self.driver.title
        self.assertIn(expect,msg)

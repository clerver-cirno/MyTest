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


class TestShoppingCart(unittest.TestCase):
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

    def test_shopping_cart(self):
        # 搜索框输入iPhone 6s
        ele_input = By.CSS_SELECTOR, "input[name=q]"
        get_element(self.driver, ele_input).send_keys("iphone 6s")
        # 点击搜索按钮
        ele_search = By.CSS_SELECTOR, 'button'
        get_element(self.driver, ele_search).click()
        # 打开详情页
        ele_page = By.CSS_SELECTOR, "a img[class=lazy-list]"
        get_element(self.driver, ele_page).click()
        time.sleep(2)
        # 加入到购物车
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(By.CSS_SELECTOR, "a[class=addcar]")).click()
        time.sleep(2)
        # 切换到弹出的窗口iframe
        iframe = get_element(self.driver, (By.XPATH, '//iframe'))
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
        # 找到'添加成功'
        ele_ct = By.CSS_SELECTOR, "div[class=conect-title]>span"
        conect_title = get_element(self.driver, ele_ct)
        print("conect_title:" + conect_title.text)
        self.assertIn("添加成功", conect_title.text)

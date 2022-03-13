import time
import unittest

from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Base import log
from Base.Base_page import BasePage
from Page.home_page import home_page
from Page.login_page import login_page


@ddt
class search_(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.lp=login_page(cls.driver)
        cls.hp=home_page(cls.driver)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()



    @file_data("../data/login.yaml")
    #登录后搜索
    def test01_search(self,**kwargs):
        username=kwargs["username"]
        pwd=kwargs["pwd"]
        prd=kwargs["prd"]
        self.lp.login_(username,pwd)
        time.sleep(2)
        self.hp.search_(prd)
        time.sleep(2)
        # el=By.CLASS_NAME,"prompt-msg"
        # # WebDriverWait(BasePage.driver, 10, 0.5).until(expected_conditions.presence_of_element_located(toast_))
        # # t = BasePage().driver.find_element_by_class_name("prompt-msg")
        # t=BasePage().toast_(el)
        # try:
        #     self.assertEqual("登录成功", t)
        #     time.sleep(3)
        #     as_ = BasePage.driver.find_element_by_class_name("top-nav-left")
        # # print(as_.text)
        # # tx=BasePage.locator(toast_el)
        # # BasePage.toast_(toast_)
        #     self.assertIn("186***424",as_.text)
        #     log.info("断言成功")
        # except Exception as e:
        #     log.error(f"断言出错，错误信息：{e}")
        #     BasePage().err_image(self.err_im)
    # @file_data("../data/search.yaml")
    # def test02_search(self,**kwargs):
    #     prd=kwargs["prd"]
    #     home_page().search_(prd)
    #     time.sleep(3)

if __name__ == '__main__':
    unittest.main()
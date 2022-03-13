import time
import unittest

from ddt import ddt, file_data
from selenium.webdriver.common.by import By

from Base import log
from Base.Base_page import BasePage
from Page.login_page import login_page

@ddt
class login_(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.err_im = "../screen/err_img.png"
    @classmethod
    def tearDownClass(cls) -> None:
        BasePage.driver.quit()
    @file_data("../data/login.yaml")
    def test01_login(self,**kwargs):
        username=kwargs["username"]
        pwd=kwargs["pwd"]
        login_page().login_(username,pwd)
        time.sleep(2)
        el=By.CLASS_NAME,"prompt-msg"
        # # WebDriverWait(BasePage.driver, 10, 0.5).until(expected_conditions.presence_of_element_located(toast_))
        # # t = BasePage().driver.find_element_by_class_name("prompt-msg")
        t=BasePage().toast_(el)
        log.info("开始断言")
        try:
            self.assertEqual("登录成功", t)
            time.sleep(3)
            as_ = BasePage().driver.find_element_by_class_name("top-nav-left")
        # print(as_.text)
        # tx=BasePage.locator(toast_el)
        # BasePage.toast_(toast_)
            self.assertIn("186***424",as_.text)
            log.info("断言成功")
        except Exception as e:
            log.error(f"断言出错，错误信息：{e}")
            BasePage().err_image(self.err_im)
if __name__ == '__main__':
    unittest.main()
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

from Base import log
from Base.Base_page import BasePage

"""
#核心页面元素对象
账号、密码、登录按钮
#核心的业务流
登录
# """
class login_page(BasePage):
#     @classmethod
#     def setUpClass(cls) -> None:
#         if BasePage().driver is None:
#

    url = "https://store.shopxo.net/login.html"
    file_ = "../screen/sc.png"
    file1_ = "../screen/sc1.png"

    # style=(By.XPATH,'//*[text()="帐号密码"]')
    # username = (By.XPATH, '//input[@placeholder="请输入用户名/手机/邮箱"]')
    # password = (By.XPATH, '//input[@placeholder="请输入登录密码"]')
    # code = (By.XPATH, '//input[@name="verify" and @type="text"]')
    # loginbutton=(By.CSS_SELECTOR,'[class="am-form form-validation-username"] [type="submit"]')

    style=By.XPATH,'//*[text()="帐号密码"]'
    username = By.XPATH, '//input[@placeholder="请输入用户名/手机/邮箱"]'
    password = By.XPATH, '//input[@placeholder="请输入登录密码"]'
    code = By.XPATH, '//input[@name="verify" and @type="text"]'
    loginbutton=By.CSS_SELECTOR,'[class="am-form form-validation-username"] [type="submit"]'

# #     #登录流程
    def login_(self,username,pwd):
        # 获取验证码
        self.get_screen(self.url, self.file_, self.file1_)
        res = self.yzm(self.file1_)
        log.info(f"正在调用的登陆业务方法  用户名：{username} 密码：{pwd} 验证码：{res}")
        self.click_(self.style)
        self.input_(self.username,username)
        self.input_(self.password,pwd)
        self.input_(self.code,res)
        self.click_(self.loginbutton)














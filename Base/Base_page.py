import ddddocr
from PIL import Image
from selenium import webdriver

# def openbrowser(type_):
#     try:
#         #反射机制
#         driver=getattr(webdriver,type_)()
#     except Exception as e:
#         print(e)
#         driver = webdriver.Chrome()
#     return driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Base import log


class BasePage:
    #构造函数
    def __init__(self,driver):
        self.driver=driver

    #访问URL
    def visit(self,url):
        log.info(f"访问网站：{url}")
        self.driver.get(url)
        self.driver.maximize_window()
    #元素定位
    def locator(self,loc):
        # return WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(*loc))
        return WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located(loc))
        # return self.driver.find_element(*loc)
    #输入内容
    def input_(self,loc,txt):
        log.info(f"正在对：{loc}元素进行点击操作")
        self.locator(loc).send_keys(txt)
    #点击
    def click_(self,loc):
        log.info(f"正在对：{loc}元素进行点击操作")
        self.locator(loc).click()
    # def print_cookie(self,url):
    #     self.visit(url)
    #     self.driver.get_cookies()
    # #跳过验证码cookie
    # def skip_login(self,url,cookie_):
    #     self.visit(url)
    #     self.driver.add_cookie(cookie_)
    #     self.driver.refresh()
    #截屏
    def get_screen(self ,url,file_,file1_):
        self.visit(url)
        self.driver.save_screenshot(file_)
        # time.sleep(3)
        el =self.driver.find_element_by_id("form-verify-img")
        location=el.location
        size=el.size
        print(location,size)
        im=Image.open(file_)
        box=location["x"],location["y"],location["x"]+size["width"],location["y"]+size["height"]
        img=im.crop(box)
        img1=img.save(file1_)
        #展示截图
        # Image._show(img1)
    #转换验证码
    def yzm(self,file1_):
        ocr=ddddocr.DdddOcr()
        with open(file1_,'rb') as f:
            img_bytes=f.read()
        res=ocr.classification(img_bytes)
        log.info(f"获取验证码：{res}")
        return res
    #toast弹框
    def toast_(self,loc):
        WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located(loc))
        t = self.driver.find_element_by_class_name('prompt-msg').text
        log.info(f"获取toast弹框内容：{t}")
        return t
    #截屏保存
    def err_image(self,err_im):
        log.info("截取错误图")
        self.driver.get_screenshot_as_file(err_im)

    #写入报告



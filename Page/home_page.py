import time

from selenium.webdriver.common.by import By

from Base import log
from Base.Base_page import BasePage
from Page.login_page import login_page


class home_page(BasePage):
    url="https://store.shopxo.net/"
    index_=By.ID,"search-input"
    search_bt=By.ID,"ai-topsearch"
    #搜索商品
    def search_(self,prd):
        log.info(f"正在调用搜索方法：商品名称{prd}")
        self.visit(self.url)
        time.sleep(2)
        self.input_(self.index_,prd)
        self.click_(self.search_bt)


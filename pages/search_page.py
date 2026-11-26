from base.page_base import PageBase
from selenium.webdriver.common.by import By

class SearchPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_home=By.XPATH,'//android.widget.TextView[@resource-id="com.netease.yanxuan:id/txt_mainpage_tab_title" and @text="首页"]'

        self.search_enter=By.CLASS_NAME,'android.widget.TextSwitcher'

        self.search_input=By.ID,'com.netease.yanxuan:id/search_input'
        self.search_button=By.ID,'com.netease.yanxuan:id/tv_search_button'

        self.success_result=By.XPATH,'//android.widget.TextView[@resource-id="com.netease.yanxuan:id/tv_goods_name"][1]'


    def search(self,content):
        self.base_click(self.back_home)
        self.base_click(self.search_enter)
        self.base_input_text(self.search_input,content)
        self.base_click(self.search_button)

    def get_success_result(self):
        return self.base_get_text(self.success_result)
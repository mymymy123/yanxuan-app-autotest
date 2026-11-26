from base.page_base import PageBase
from selenium.webdriver.common.by import By


class EnterHomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.agree_loc=By.ID,'com.netease.yanxuan:id/btn_alert_positive'
        self.skip_loc=By.XPATH, '//android.widget.TextView[@text="跳过"]'
        self.info_confirm=By.ID,'com.android.permissioncontroller:id/permission_allow_button'

    def enter_home(self):
        
        self.base_click(self.agree_loc)
        self.base_click(self.info_confirm)
        self.base_click(self.skip_loc)

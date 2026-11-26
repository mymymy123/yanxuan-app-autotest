from base.page_base import PageBase
from selenium.webdriver.common.by import By

class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.person_button=By.XPATH, '//android.widget.TextView[@resource-id="com.netease.yanxuan:id/txt_mainpage_tab_title" and @text="个人"]'
        self.other_button=By.XPATH, '(//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/img_icon"])[2]'
        self.other_way=By.ID, 'com.netease.yanxuan:id/newOtherLoginTypes'
        self.scheme_check=By.ID, 'com.netease.yanxuan:id/check_box'
        self.mail_way=By.XPATH, '(//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/img_icon"])[4]'
        self.username=By.ID, 'com.netease.yanxuan:id/account_edit'
        self.password=By.ID, 'com.netease.yanxuan:id/password_edit'
        self.login_button=By.ID, 'com.netease.yanxuan:id/btn_login_content'

        self.success_result=By.ID,'com.netease.yanxuan:id/user_name'

        self.fail_result= (By.XPATH, '//android.widget.Toast')

    def enter_login(self):
        self.base_click(self.person_button)
        self.base_click(self.other_button)
        self.base_click(self.other_way)
        self.base_click(self.scheme_check)
        self.base_click(self.mail_way)

    def login(self,username,password):
        self.base_input_text(self.username,username)
        self.base_input_text(self.password,password)
        self.base_click(self.login_button)

    def get_success_result(self):
        return self.base_get_text(self.success_result)

    def get_fail_result(self):
            return self.base_get_toast(self.fail_result)

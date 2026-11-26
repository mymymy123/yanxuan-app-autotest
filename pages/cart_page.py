from selenium.webdriver.common.by import By
from base.page_base import PageBase

class CartPage(PageBase):
    """购物车页面"""
    def __init__(self, driver):
        super().__init__(driver)
        # 第一个商品图
        self.goods_img = (By.XPATH, '(//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/img_goods"])[1]')
        # 位置权限
        self.location_btn = (By.ID, 'com.netease.yanxuan:id/btn_alert_positive')
        self.location_agree=(By.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        # 点击加入购物车按钮
        self.cart_btn1 = (By.XPATH, '//android.widget.TextView[@text="加入购物车"]')
        self.cart_btn2 = (By.ID, 'com.netease.yanxuan:id/button')
        # 购物车toast提示结果
        self.result_loc = (By.XPATH, '//android.widget.Toast')
        # 返回首页：3次操作
        self.back_loc1 = (By.ID, 'com.netease.yanxuan:id/nav_left_text')
        self.back_loc2 = (By.ID, 'com.netease.yanxuan:id/search_bar_return')
        # back_loc3 = (AppiumBy.ID, 'com.netease.yanxuan:id/search_bar_return')

    def enter_goods_detail(self):
        """进入商品详情页"""
        self.base_click(self.goods_img)
        if self.is_element_exist(self.location_btn):
            self.base_click(self.location_btn)
            self.base_click(self.location_agree)
    def add_cart(self):
        """加入购物车"""
        self.base_click(self.cart_btn1)
        self.base_click(self.cart_btn2)

    def back_home(self):
        """返回首页"""
        self.base_click(self.back_loc1)
        self.base_click(self.back_loc2)
        self.base_click(self.back_loc2)
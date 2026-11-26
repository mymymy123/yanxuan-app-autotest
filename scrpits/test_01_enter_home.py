from pages.enter_home_page import EnterHomePage


class TestEnterHome:

    def test_01_enter_home(self,first_app_driver):
        self.enter=EnterHomePage(first_app_driver)
        self.enter.enter_home()
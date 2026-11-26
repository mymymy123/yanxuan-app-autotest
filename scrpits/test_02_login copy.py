from pages.login_page import LoginPage
from base import logger
from utils.tools import read_json
import pytest
class TestLogin:

    @pytest.mark.parametrize('username,password,expect_result,img',read_json('login_data.json'))
    def test_01_login(self,login_fix,username,password,expect_result,img):
        login_fix.login(username,password)
        result=login_fix.get_success_result() or login_fix.get_fail_result()
        logger.info(f'登录结果为：{result}')
        assert expect_result in result
        login_fix.base_get_shot(img)


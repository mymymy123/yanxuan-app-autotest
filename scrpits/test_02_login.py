from pages.login_page import LoginPage
from base import logger
from config import *
class TestLogin:

    def test_01_login_success(self,login_fix):
        login_fix.login(EMAIL,PASSWORD)
        result=login_fix.get_success_result()
        logger.info(f'登录结果为：{result}')
        assert '用户' in result
        login_fix.base_get_shot('login_success')

    def test_02_login_fail_pwd(self,login_fix):
            login_fix.login(EMAIL,PASSWORD)
            result=login_fix.get_fail_result()
            logger.info(f'登录结果为：{result}')
            assert '账号或密码' in result
            login_fix.base_get_shot('login_fail_pwd')

    def test_03_login_fail_username(self,login_fix):
                login_fix.login(EMAIL,PASSWORD)
                result=login_fix.get_fail_result()
                logger.info(f'登录结果为：{result}')
                assert '格式错误' in result
                login_fix.base_get_shot('login_fail_username')
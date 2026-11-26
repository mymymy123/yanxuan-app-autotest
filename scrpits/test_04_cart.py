from base import logger

class TestCart:

    def test_01_add(self,cart_fix):
        cart_fix.add_cart()
        result=cart_fix.base_get_toast(cart_fix.result_loc)
        logger.info(f'加入购物车结果：{result}')
        assert '加入购物车成功' in result
        cart_fix.base_get_shot('add_cart')
        cart_fix.back_home()
from base import logger

class TestSearch:

    def test_01_search(self,search_fix):
        search_fix.search('毛巾')
        result=search_fix.get_success_result()
        logger.info(f'搜索结果为：{result}')
        assert '毛巾' in result
        search_fix.base_get_shot('search')
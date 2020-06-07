#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:get_user_tag_testcase.py
# @time:2020/6/7 8:36 下午

import unittest
from utils.config_utils import config
from utils import common_api

class GetUsertagTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.get_host_path
    def tearDown(self) -> None:
        pass

    def test_get_user_tag(self):
        token_id = common_api.get_access_token_value()
        res_obj = common_api.get_user_tag_api(token_id)
        self.assertEqual(res_obj.json()['tags'][3]['id'], 103)

if __name__ == "__main__":
    unittest.main()
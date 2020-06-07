#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:create_user_tag_testcase.py
# @time:2020/6/7 11:27 上午

import unittest
from utils.config_utils import config
from utils import common_api

class CreateUsertagTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.get_host_path
    def tearDown(self) -> None:
        pass

    def test_create_user_tag(self):
        token_id = common_api.get_access_token_value()
        res_obj = common_api.create_user_tag_api(token_id, '新建标签10005')
        self.assertEqual(res_obj.json()['tag']['name'].encode('utf-8').decode('unicode_escape'), '新建标签10005')

if __name__ == "__main__":
    unittest.main()
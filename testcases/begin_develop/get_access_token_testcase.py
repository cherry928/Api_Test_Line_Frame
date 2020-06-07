#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:get_access_token_testcase.py
# @time:2020/6/7 11:12 上午

import unittest
from utils.config_utils import config
from utils import common_api

class GetAccesstokenTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.get_host_path
    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        res_obj = common_api.get_access_token_api('client_credential',
                                                  'wx5189359b0e0ddd89',
                                                  '11d4de7719a2276becf27ab573263061')
        self.assertEqual(res_obj.json()['expires_in'], 7200)

    def test_appid_error(self):
        res_obj = common_api.get_access_token_api('client_credential',
                                                  'wx5189359b0e0ddd8',
                                                  '11d4de7719a2276becf27ab573263061')
        self.assertEqual(res_obj.json()['errcode'], 40013)

if __name__ == "__main__":
    unittest.main()
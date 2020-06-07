#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:common_api.py
# @time:2020/6/7 11:03 上午

import requests
from utils.config_utils import config

def get_access_token_api(grant_type, appid, secret):
    api_url = config.get_host_path + '/cgi-bin/token'
    get_params_data = {
        'grant_type': grant_type,
        'appid': appid,
        'secret': secret
    }
    response_obj = requests.get(url=api_url,
                                params=get_params_data)
    return response_obj

def get_access_token_value():
    response_obj = get_access_token_api('client_credential',
                                        'wx5189359b0e0ddd89',
                                        '11d4de7719a2276becf27ab573263061')
    return response_obj.json()['access_token']

def create_user_tag_api(token_id, tag_name):
    api_url = config.get_host_path + '/cgi-bin/tags/create'
    get_param_data = {'access_token': token_id}
    header_info = {'Content-Type':'application/json'}
    post_param_data = {"tag": {"name": tag_name}}
    respon_obj = requests.post(url=api_url,
                               params=get_param_data,
                               headers=header_info,
                               json=post_param_data)
    return respon_obj

def get_user_tag_api(token_id):
    api_url = config.get_host_path + '/cgi-bin/tags/get'
    get_param_data = {'access_token': token_id}
    response_obj = requests.get(url=api_url,
                                params=get_param_data)
    return response_obj

def update_user_tag_api(token_id, tag_id, tag_name):
    api_url = config.get_host_path + '/cgi-bin/tags/update'
    get_param_data = {'access_token': token_id}
    header_info = {'Content-Type':'application/json'}
    post_param_data = {   "tag" : {     "id" : tag_id,     "name" : tag_name   } }
    respon_obj = requests.post(url=api_url,
                               params=get_param_data,
                               headers=header_info,
                               json=post_param_data)
    return respon_obj

def delete_user_tag_api(token_id, tag_id):
    api_url = config.get_host_path + '/cgi-bin/tags/delete'
    get_param_data = {'access_token': token_id}
    header_info = {'Content-Type':'application/json'}
    post_param_data = {   "tag" : {     "id" : tag_id} }
    respon_obj = requests.post(url=api_url,
                               params=get_param_data,
                               headers=header_info,
                               json=post_param_data)
    return respon_obj

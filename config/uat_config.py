# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:27
# @Author  : linwei
from config.common_config import CommonConfig


class UatConfig(CommonConfig):
    """联调环境"""
    BASE_URL1 = 'http://192.168.1.1:8001'
    BASE_URL2 = 'http://192.168.1.1:8002'
    BASE_URL3 = 'http://192.168.1.1:8003'

    query_url = {
        'HTHL接口请求': 'http://192.168.1.9:9999',
        '恒天管理系统': 'http://192.168.1.8:18081',
        '智能账簿管理系统': 'http://192.168.1.8:18080',
        'ZNZB接口请求': 'http://192.168.1.8:19999',
        '任务调度中心接口请求': 'http://192.168.1.8:9080',
        '企业前端接口请求': 'http://192.168.1.8:18082',
        '账簿后台登录地址': 'http://192.168.1.8:18080/smart-account/#/login',
        '管理后台登录地址': 'http://192.168.1.8:18081/htbms-manager/#/login',
        '企业前端登录地址': 'http://192.168.1.8:18082/htbms-enterprise/#/login',
        '外放提现地址': 'http://192.168.1.8:18082/htbms-enterprise/#/pay/withdrawal',
    }

    auto_setToken = {
        'hthl_sys_get_token': query_url.get('恒天管理系统') + '/auth/oauth/token',
        'hthl_sys_api_get_token': query_url.get('HTHL接口请求') + '/auth/oauth/token',
        'account_book_get_token': query_url.get('智能账簿管理系统') + '/acc-auth/oauth/token',
        'account_book_api_get_token': query_url.get('ZNZB接口请求') + '/acc-auth/oauth/token',
        'hthl_enterprise_api_get_token': query_url.get('企业前端接口请求') + '/auth/oauth/token',

    }

    TestHtbms = {
        'host': "108.174.60.167",
        'user': "root",
        'password': "hthl#2022",
        'port': 13306,
        'db': "test_htbms"  # 连接数据的库名
    }

    SmartAccountUat = {
        'host': "108.174.60.167",
        'user': "root",
        'password': "hthl#2022",
        'port': 13306,
        'db': "smart_account_uat"  # 连接数据的库名
    }

    TestQfzl = {
        'host': "108.174.60.167",
        'user': "root",
        'password': "hthl#2022",
        'port': 13306,
        'db': "test_qfzl"  # 连接数据的库名
    }


if __name__ == '__main__':
    print(UatConfig.TestHtbms)
    print(UatConfig.SmartAccountUat)
    print(UatConfig.TestQfzl)

# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:27
# @Author  : linwei
from config.common_config import CommonConfig
import time


class DevConfig(CommonConfig):
    """测试环境"""
    BASE_URL1 = 'http://192.168.1.8'
    BASE_URL2 = 'http://192.168.1.9'

    server = 'dev'
    x_platform_code = '51320000050261200XSS'  # 51320000050261200XSS   911100007693890511001
    privateKey = 'MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDidp/sWbVq8eR2E1HrvaEH0/ckdN0Z5RcdzHyFRWrXB87rJV6irbcc+BB2hN+lypkZjwZ4tqTyeQO7qon8KkMEfdTHKxxn080niucNtTsRvcj5GkKqCzoFv6eqB49XVOnrnBJFVeUNO7PGz/gZa3xAxQrio5eIZTj+rbTb/SN1HiweUy5uQ3UHm4LvrDncPrsd48M2Sgrj3x8MhFbye7MCWTEDOWuU/jFV4OMNjr7me3Mu46PGXHCWbkkuuSrd9b3cXPj6MxEDBvln6ilQ3UW78XlyM8Ideru8cRLBMiiTSd48SLJWWdu+oac1cGBSfrQso4SWYuXA+PiNexkWF8GLAgMBAAECggEBAIO1wmVP93dvoBQcQHT/IPzQhtipLz60QrGOEI3iRbUyUWHpphSvO+SZUdnchcaDAnAfAwCKGXz8bPNkyEPkwH2IQYxkwmyQfq0U2DTcxrIW0yAt6b/EL8bQJM96/h8ov7PMXcP9pO4BXxmuMvl1zhpNf3s48hTd6jwVAy8/FrQx89llm3jErwOU9OBFPOCib2DbUcEOw1pXmJig+TJuy7sMuwa4psWqrpmtdO1SupIeRuUwbajgCrw9h9Pfm0yan0TGyugmXmeyCY9fMzx//3FGKRPZfgpVys+2i8DwtD8F/NKCYPxhi3fugtiAo84879pw30XRRUNxacRgJkP2gCECgYEA+1Rm9z2tbi1qfyAzT3PrzSbJjNED4xm7DkQyFXMuzyV2tJ58E6mTjWivFDo9klMcaapZm8veKmoj+zINIiVahcnDnqH4CXrZYzZ0a3zyLfiaw+CuT0ozNAY9Ir0IIcSYpR6JyWRYPbj3cbpYBQmLMNwSpBEB6P8E9YqRmntbG20CgYEA5qvuYsa8SNTz8mS42PWWLGe0L+skAb2n0gYFP1oeZgNaUX5DjYAbRz0XfT5Z2jNnCUePMnGhM6JO2CxH/jchFwhE1iyXuYBG1OoS1SYhqCEB6AjyiTtwAi5IK7bsVfRejzdhcuFi85QQmds/7VwFSKUbONz0zoR+fptcMR+9/dcCgYBNFf0i1hsMkQd6CGFUfESVvtDQzQb5L9osrQQDijmQNXhsO7Pov/lOxQ32EUrzR2SOkD49x9DTh4yTri1TDMvv/wtt61XNao2knX4lvcP2D6tAavhrv2FnEobL0djdqpP7CRvP1mQuQj469qGqodu8V7Or+L9yPE3EFgVEsZMnHQKBgQCENDv/Xrmg4HQkE3gh2LdGIfWSlSjg2orpg0vUoFjVzMwh8sTSv35i2O+yd17WASnnlpzKo3dpeXfIy7BDUeNkKPgS7CHVTmDKPJGomh8mFizaiO5AmtE6Xr48V62iIdlkKbBvQCAPTGgrVg6QgnIAzagJchHYnvVEqNQwz2l7pwKBgQDjaMsUduf5mM5gsWuMPDfIGdtKG5+e+Z3rlszYK0zYKnkByDAik9H9EaTOAQMeLoE3Sr0XCID6UgQSeWm3pCQWCydWD/0HXkA7qb28ln6vzcWdE+o27+6PG7OL2bIfSmMoqyzaNuWX1q+WMJOzsXJVEq6Hnt3y4GkDAP6hEtHWzg=='
    interface_address = BASE_URL2 + ":9999/api/v1"

    query_url = {
        'HTHL接口请求': BASE_URL2 + ':9999',
        '恒天管理系统': BASE_URL1 + ':18081',
        '智能账簿管理系统': BASE_URL1 + ':18080',
        'ZNZB接口请求': BASE_URL1 + ':19999',
        '任务调度中心接口请求': BASE_URL1 + ':9080',
        '企业前端接口请求': BASE_URL1 + ':18082',
        '账簿后台登录地址': BASE_URL1 + ':18080/smart-account/#/login',
        '管理后台登录地址': BASE_URL1 + ':18081/htbms-manager/#/login',
        '企业前端登录地址': BASE_URL1 + ':18082/htbms-enterprise/#/login',
        '外放提现地址': BASE_URL1 + ':18082/htbms-enterprise/#/pay/withdrawal',
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
    # print(DevConfig.query_url)
    print(DevConfig.auto_setToken)
    # print(DevConfig.TestHtbms)
    # print(DevConfig.SmartAccountUat)
    # print(DevConfig.TestQfzl)

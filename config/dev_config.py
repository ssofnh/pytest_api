# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:27
# @Author  : linwei
from config.common_config import CommonConfig


class DevConfig(CommonConfig):
    """测试环境"""
    BASE_URL1 = 'http://192.168.1.1:8001'
    BASE_URL2 = 'http://192.168.1.1:8002'
    BASE_URL3 = 'http://192.168.1.1:8003'

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
    print(DevConfig.TestHtbms)
    print(DevConfig.SmartAccountUat)
    print(DevConfig.TestQfzl)

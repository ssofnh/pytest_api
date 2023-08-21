# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:27
# @Author  : linwei
from config.common_config import CommonConfig


class UatConfig(CommonConfig):
    """联调环境"""
    BASE_URL1 = 'http://192.168.1.1:8001'
    BASE_URL2 = 'http://192.168.1.1:8002'
    BASE_URL3 = 'http://192.168.1.1:8003'

    MYSQL_1 = {
        'MYSQL_HOST': "192.168.1.1",
        'MYSQL_USER': "root",
        'MYSQL_PASSWORD': "123456",
        'MYSQL_PORT': 3306,
        'MYSQL_DATABASE': "xxx1"  # 连接数据的库名
    }

    MYSQL_2 = {
        'MYSQL_HOST': "192.168.1.1",
        'MYSQL_USER': "root",
        'MYSQL_PASSWORD': "123456",
        'MYSQL_PORT': 3306,
        'MYSQL_DATABASE': "xxx2"  # 连接数据的库名
    }

    MYSQL_3 = {
        'MYSQL_HOST': "192.168.1.1",
        'MYSQL_USER': "root",
        'MYSQL_PASSWORD': "123456",
        'MYSQL_PORT': 3306,
        'MYSQL_DATABASE': "xxx3"  # 连接数据的库名
    }

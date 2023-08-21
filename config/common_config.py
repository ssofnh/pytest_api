# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:07
# @Author  : linwei
from config.file_path_config import ACCESS_TOKEN_PATH
from utils.ReadWriteFile_Helper import ReadWriteFile


class CommonConfig:
    """多套环境的公共配置"""
    version = "v1.0"

    # 回调地址
    notifyUrl = "http://django.hthl.eu.org/api_system/v1/callback"
    # 跳转地址（支付成功）
    returnUrl = "http://django.hthl.eu.org/api_system/v1/callback"

    hthl_sys_token = None
    hthl_sys_api_token = None
    account_book_token = None
    account_book_api_token = None

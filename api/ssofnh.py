# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 14:25
# @Author  : linwei

import os

import pytest

from config.dev_config import DevConfig
from config.prod_config import ProdConfig
from config.uat_config import UatConfig
from core.rest_client import RestClient

class Ssofnh(RestClient):

    def __init__(self, env_config, **kwargs):
        '''动态获取api_root_url'''
        self.env_config = env_config
        api_root_url = self.env_config.query_url.get("恒天管理系统")
        super(Ssofnh, self).__init__(api_root_url, **kwargs)

    def list_all_users(self, **kwargs):
        return self.post("/auth/oauth/token", **kwargs)

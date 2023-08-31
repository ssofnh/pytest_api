# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 14:25
# @Author  : linwei

import json
from core.rest_client import RestClient
from utils.encrypt_api.ProductEnum import ProductEnum
from utils.encrypt_api.Api_Public_Method import Api_Public_Method


class Ssofnh(RestClient):

    def __init__(self, env_config, **kwargs):
        '''动态获取api_root_url'''
        self.env_config = env_config
        self.api_root_url = self.env_config.interface_address
        super(Ssofnh, self).__init__(self.api_root_url, **kwargs)

        type = ProductEnum.WITHDRAW_QUERY
        # 初始化 Api_Public_Method 类实例
        self.api_public_method = Api_Public_Method(server=self.env_config.server,
                                                   type=type,
                                                   x_platform_code=self.env_config.x_platform_code,
                                                   privateKey=self.env_config.privateKey,
                                                   x_product_code=type.value[0])

    def execute_interface_e02(self, data, **kwargs):
        # 使用 Api_Public_Method 类实例的加密方法
        send_data, pairs_dict, headers = self.api_public_method.Interface_template(data)
        # 使用RestClient的请求方法发送请求
        return self.post(f"{self.api_public_method.type.value[1]}",
                         data=json.dumps(send_data if send_data else pairs_dict, separators=(',', ':')),
                         headers=headers,
                         verify=False, **kwargs)

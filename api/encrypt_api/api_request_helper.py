# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 14:54
# @Author  : linwei


import json
import pytest
from common.logger import logger
from core.rest_client import RestClient
from utils.encrypt_api.Api_Public_Method import Api_Public_Method
from utils.encrypt_api.ProductEnum import ProductEnum


class ApiRequestHelper(RestClient):
    # 所有下游接口的请求都需要调用此类

    def __init__(self, env_config, type, **kwargs):
        '''
        env_config：读取根目录下的conftest.py的夹具 EnvConfig;
        type: 指定请求哪个接口；
        实例化接口请求的类：动态获取接口请求地址 api_root_url;
        '''
        # 动态获取api_root_url
        self.env_config = env_config
        self.api_root_url = self.env_config.interface_address
        super(ApiRequestHelper, self).__init__(self.api_root_url, **kwargs)

        # 初始化 Api_Public_Method 类实例
        self.api_public_method = Api_Public_Method(type=type,
                                                   x_platform_code=self.env_config.x_platform_code,
                                                   privateKey=self.env_config.privateKey,
                                                   x_product_code=type.value[0])

    def execute_api_request(self, data, **kwargs):
        # 使用 Api_Public_Method 类实例的加密方法
        send_data, pairs_dict, headers = self.api_public_method.Interface_template(data)
        logger.info(f"接口请求报文：{send_data if send_data else pairs_dict}")
        # 使用RestClient的请求方法发送请求
        return self.post(f"{self.api_public_method.type.value[1]}",
                         data=json.dumps(send_data if send_data else pairs_dict, separators=(',', ':')),
                         headers=headers,
                         verify=False, **kwargs)


if __name__ == '__main__':
    # 使用示例如下：
    @pytest.fixture(scope="session")
    def e02(EnvConfig):
        '''实例化加密接口对象'''
        return ApiRequestHelper(env_config=EnvConfig, type=ProductEnum.WITHDRAW_QUERY)

    def test_E02(e02):
        '''测试用例使用夹具，传入data明文数据即可；'''
        data = {
            'clientOrderNo': '3242384723143',  # 请求流水号;
            'origClientOrderNo': '',  # 原申请流水号;
            'origServerOrderNo': '714064449509384192',  # 原申请服务端流水号;
        }
        r = e02.execute_interface(data=data)
        logger.info(f"接口返回报文：{r.text}")
        assert r.status_code == 200

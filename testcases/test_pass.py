# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 11:17
# @Author  : linwei
import pytest

from api.ssofnh import Ssofnh

# @pytest.mark.test
# def test_pass(EnvConfig):
#     pass
#     print(EnvConfig.hthl_sys_token)
#     assert True
#





@pytest.fixture(scope="session")
def ssofnh(EnvConfig):
    '''
    读取根目录下的conftest.py的夹具：EnvConfig；
    实例化接口请求的类：动态获取接口请求地址
    '''
    return Ssofnh(EnvConfig)

@pytest.mark.test
def test_qq(ssofnh):
    headers = {"Authorization": "Basic dGVzdDp0ZXN0"}
    params = {"grant_type": "password", "scope": "server"}
    data = {"username": "linwei", "password": "123456"}
    r = ssofnh.list_all_users(data=data, params=params, headers=headers, verify=False, timeout=2)
    assert r.status_code == 200

@pytest.mark.test1
def test_ww():
    # E02验证可以使用
    data = {
        'clientOrderNo': '3242384723143',  # 请求流水号;
        'origClientOrderNo': '',  # 原申请流水号;
        'origServerOrderNo': '714064449509384192',  # 原申请服务端流水号;
    }
    # r = ssofnh.execute_interface_e02(data=data)
    # assert r.status_code == 200

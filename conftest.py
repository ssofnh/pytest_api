# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:44
# @Author  : linwei

import pytest

from common.mysql_operate import MysqlDb
from config import dev_config, uat_config, prod_config
from config.access_token.Initialize_access_token import auto_setTokens
from config.file_path_config import ACCESS_TOKEN_PATH
from utils.ReadWriteFile_Helper import ReadWriteFile


@pytest.fixture(scope="session", autouse=True)
def EnvConfig(request):
    '''读取环境配置'''
    env = request.config.getoption("--env")
    if env == "dev":
        # print("测试环境")
        return dev_config.DevConfig
    elif env == "uat":
        # print("联调环境")
        return uat_config.UatConfig
    elif env == "prod":
        # print("生产环境")
        return prod_config.ProdConfig
    else:
        raise ValueError(f"Invalid environment: {env}. Use --env=dev or --env=uat or --env=prod.")


def pytest_addoption(parser):
    '''添加命令行参数'''
    parser.addoption("--env", action="store", default="dev", help="Specify the environment: dev or uat or prod.")


@pytest.fixture(scope="session", autouse=True)
def db(EnvConfig):
    '''初始化数据库'''
    db_test_htbms = MysqlDb(db_conf=EnvConfig.TestHtbms)
    db_smart_account_uat = MysqlDb(db_conf=EnvConfig.SmartAccountUat)
    yield db_test_htbms, db_smart_account_uat


@pytest.fixture(scope="session", autouse=True)
def Access_token(EnvConfig):
    '''初始化token'''
    # 将token写入文件
    auto_setTokens(auto_setToken=EnvConfig.auto_setToken).get_token()
    # 读取token赋值给变量
    EnvConfig.hthl_sys_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_sys_token.md').read_file()
    EnvConfig.hthl_sys_api_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_sys_api_token.md').read_file()
    EnvConfig.account_book_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'account_book_token.md').read_file()
    EnvConfig.account_book_api_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'account_book_api_token.md').read_file()
    # EnvConfig.hthl_enterprise_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_enterprise_token.md').read_file()
    yield

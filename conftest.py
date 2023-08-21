# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:44
# @Author  : linwei

import pytest

from common.mysql_operate import MysqlDb
from config import dev_config, uat_config, prod_config


@pytest.fixture(scope="session", autouse=True)
def EnvConfig(request):
    '''环境切换的配置'''
    env = request.config.getoption("--env")
    if env == "test":
        return dev_config.DevConfig
    elif env == "uat":
        return uat_config.UatConfig
    elif env == "prod":
        return prod_config.ProdConfig
    else:
        raise ValueError(f"Invalid environment: {env}. Use --env=test or --env=uat or --env=prod.")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help="Specify the environment: test or uat or prod.")


@pytest.fixture(scope="session")
def db(EnvConfig):
    '''初始化数据库'''
    config = EnvConfig()
    print(config.TestHtbms)
    print(config.SmartAccountUat)
    db_test_htbms = MysqlDb(db_conf=config.TestHtbms)
    db_smart_account_uat = MysqlDb(db_conf=config.SmartAccountUat)

    yield db_test_htbms, db_smart_account_uat

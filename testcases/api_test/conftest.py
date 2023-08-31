# import pytest
# from testcases.conftest import api_data
#
#
# @pytest.fixture(scope="function")
# def testcase_data(request):
#     testcase_name = request.function.__name__
#     return api_data.get(testcase_name)

import pytest

from api.encrypt_api.api_request_helper import ApiRequestHelper
from utils.encrypt_api.ProductEnum import ProductEnum


@pytest.fixture(scope="session")
def E02(EnvConfig):
    return ApiRequestHelper(env_config=EnvConfig, type=ProductEnum.WITHDRAW_QUERY)

@pytest.fixture(scope="session")
def A01(EnvConfig):
    return ApiRequestHelper(env_config=EnvConfig, type=ProductEnum.ENTERPRISE_REGISTER)

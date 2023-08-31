# -*- coding: utf-8 -*-
# @Time    : 2023/8/29 15:04
# @Author  : linwei

import os
import pytest


if __name__ == '__main__':
    # 运行测试用例并生成 Allure 报告
    pytest_args = ['-s', '-m', 'test2', '--env=dev', '--capture=no', '--alluredir', 'report/allure_raw']
    pytest.main(pytest_args)

    # 启动服务查看测试报告
    os.system('allure serve report/allure_raw')

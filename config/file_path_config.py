# -*- coding: utf-8 -*-
# @Time    : 2023/4/14 15:01
# @Author  : linwei

import os

# -----------------------------------------------------------------------------------
# file_path_config.py 所在目录路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 项目根路径
PROJECT_DIR = os.path.dirname(BASE_DIR)

# 驱动目录
DRIVERS_DIR = os.path.join(PROJECT_DIR, "drivers")

# 录制视频的存放目录
VIDEOS_DIR = os.path.join(PROJECT_DIR, "videos")

# DDXFOT
DDXFOT_PATH = os.path.join(DRIVERS_DIR, "DDXFOT", "Drivers", r"1.Simple", "DD94687.64.dll")

# 上传文件路径
UPLOAD_PATH = os.path.join(PROJECT_DIR, "upload_and_download_files", "upload")

# 下载文件路径
DOWNLOAD_PATH = os.path.join(PROJECT_DIR, "upload_and_download_files", "download")

# access_token的存放路径, 接口请求使用
ACCESS_TOKEN_PATH = os.path.join(PROJECT_DIR, "config", "access_token")

# 任务调度中心：执行调度
TASK_ID_JSON_PATH = os.path.join(PROJECT_DIR, "api", "task_dispatch_center")

# 企业数据存放路径
ENTERPRISE_DATA_PATH = os.path.join(PROJECT_DIR, "testdata", "enterprise_data")

# 测试报告存放目录
REPORT_DIR = os.path.join(PROJECT_DIR, "report")

# 谷歌浏览器驱动
CHROME_DRIVERS_DIR = os.path.join(PROJECT_DIR, "drivers", "chrome")

# 元素定位代码生成
# PAGE = os.path.join(PROJECT_DIR, "page")

# 元素定位管理
# PAGEELEMENT_PATH = os.path.join(PAGE, "pageelement")
#


# 日志
# LOG_DIR_PATH = os.path.join(PROJECT_DIR, "logs")

# 测试用例数据目录
# TEST_DATA_EXCEL_DIR = os.path.join(XIBAUTOTEST_DIR, "testdata")

# 测试用例代码目录
# TESTCASES_DIR = os.path.join(XIBAUTOTEST_DIR, "testcases")

# 截图目录
# SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "screenShots")
# 谷歌浏览器驱动完整路径
# CHROME_DRIVER_PATH = os.path.join(DRIVERS_DIR, "chrome", "chromedriver.exe")
# 测试代码路径
# XIBAUTOTEST_DIR = os.path.join(PROJECT_DIR, "xibautotest")


if __name__ == '__main__':
    print(BASE_DIR)
    print(PROJECT_DIR)
    print(UPLOAD_PATH)
    print(DOWNLOAD_PATH)
    print(ACCESS_TOKEN_PATH)
    print(TASK_ID_JSON_PATH)
    print(DDXFOT_PATH)
    print(VIDEOS_DIR)
    print(ENTERPRISE_DATA_PATH)

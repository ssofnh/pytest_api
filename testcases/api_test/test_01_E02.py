# -*- coding: utf-8 -*-
# @Time    : 2023/8/29 10:57
# @Author  : linwei
import pytest
import allure
from common.logger import logger


@pytest.mark.test2
@allure.feature("编辑分类文章")
@allure.story("登录-编辑文章分类，重复保存，保存失败")
@allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")  # 禅道bug地址
@allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-5-1.html")  # 禅道用例连接地址
def test_E02(E02):
    data = {
        'clientOrderNo': E02.api_public_method.clientOrderNo(),  # 请求流水号;
        'origClientOrderNo': '',  # 原申请流水号;
        'origServerOrderNo': '714064449509384192',  # 原申请服务端流水号;
    }
    r = E02.execute_api_request(data=data)
    logger.info(f"接口返回报文：{r.text}")
    assert r.status_code == 200


@pytest.mark.test2
def test_A01(A01):
    data = {
        'clientOrderNo': A01.api_public_method.clientOrderNo(),  # 注册申请流水号;
        'socialCreditCode': '521302125098548500',  # 社会统一信用代码;
        'name': '企业注册（哈哈哈001）有限责任公司',  # 企业名称;
        'businessLicense': 'https://dev-htbms.oss-cn-hangzhou.aliyuncs.com/prev-data/20221030172628.jpg',
        # 营业执照文件: 上传能下载文件的oss链接地址;
        'businessLicenseValidityTimeStart': '',  # 营业执照有效期(起始日期): 格式：yyyyMMdd;
        'businessLicenseValidityTimeEnd': '',  # 营业执照有效期（结束日期）:格式：yyyyMMdd; 长期：99991231;
        'businessScope': '',  # 营业范围: 和营业执照上的文字一致
        'legalPersonName': '',  # 法人姓名;
        'legalPersonIdNo': '123456789012345678',  # 法人证件号码;
        'legalPersonIdFrontPhoto': 'https://test-htbms.oss-cn-hangzhou.aliyuncs.com/enterprise/20220923/032be5d14c024675bc05c0a57a6b6d2d.jpg',
        # 法人证件照（正面）文件: 上传能下载文件的oss链接地址;
        'legalPersonIdReversePhoto': 'http://tcpjw.oss-cn-shanghai.aliyuncs.com/c5b78f51dc7545388b4fb357518a16b6.jpg',
        # 法人证件照（反面）文件: 上传能下载文件的oss链接地址;
        'legalPersonIdValidityTimeStart': '',  # 法人证件有效期（起始日期）: 格式：yyyyMMdd;
        'legalPersonIdValidityTimeEnd': '',  # 法人证件有效期（结束日期）: 格式：yyyyMMdd;
        'legalPersonConnectPhone': '',  # 法人联系手机号;
        'legalPersonConnectAddress': '',  # 法人联系地址;
        'address': '',  # 企业地址;
        'email': '',  # 企业邮箱;
        'connectPhone': '',  # 企业联系电话;
        'registerCapital': 1,  # 注册资本金额: 单位/分;
        'actuallyReceivedCapital': 1,  # 实收资本金额: 单位/分;
        'numberOfEmployees': 1,  # 职工人数: 人数大于0;
        'annualSalesAmount': 1,  # 年销售金额: 单位/分;
        'totalAssets': 1,  # 资产总金额: 单位/分;
        'industry': '',  # 所属行业: 见附录;
        'ipAddress': '',  # Ip地址;
        'macAddress': '',  # Mac地址;
        'platformAuthenticationLevel': '23',  # 平台认证等级: 0-100的整数;
        # 企业联系人信息: 联系人信息填写完整或者null;
        'connectPerson': {
            'authorizeEntrustFile': 'http://tcpjw.oss-cn-shanghai.aliyuncs.com/c5b78f51dc7545388b4fb357518a16b6.jpg',
            # 授权委托文件: 上传能下载文件的oss链接地址;
            'name': '123',  # 企业联系人姓名;
            'idNo': '123',  # 企业联系人证件号码;
            'idValidityTimeStart': '123',  # 企业联系人证件有效期（起始日期）: 格式：yyyyMMdd;
            'idValidityTimeEnd': '123',  # 企业联系人证件有效期（结束日期）: 格式：yyyyMMdd;
            'idFrontPhoto': '123',  # 企业联系人证件照（正面）文件: 上传能下载文件的oss链接地址;
            'idReversePhoto': '123',  # 企业联系人证件照（反面）文件: 上传能下载文件的oss链接地址;
            'connectPhone': '123',  # 企业联系人联系手机号码;
            'connectAddress': '123'  # 企业联系人联系地址;
        },
        'publicAccountNo': '15000100717139',  # 企业对公账户账号;
        'publicAccountSettleUnitNo': '307584007998',  # 企业对公账户清算联行号;
        # 增信材料列表;
        'creditMaterials': [
            # {
            #     'type':'01',  # 老客户推荐函;
            #     'dataType':'',  # 材料数据类型:  0:数据, 1:文件;
            #     'data':'',  # 材料数据值:
            #         # 当材料数据类型为文件时，上传能下载文件的oss链接地址,
            #         # 当材料数据类型为数据时，根据材料类型传对应数据,
            #         # 法人人脸活检结果 --- 0：未检测；1：检测通过；2：检测不通过,
            #         # 企业联系人人脸活检结果 --- 0：未检测；1：检测通过；2：检测不通过;
            # },
            # {
            #     'type': '02',  # 税务登记材料;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '03',  # 企业门头照;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '04',  # 企业办公场地照片;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '05',  # 前期银行流水;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '06',  # 前期票据流水;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '07',  # 法人视频;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '08',  # 授权人视频;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '09',  # 法人人脸活检结果;
            #     'dataType': '',
            #     'data': '',
            # },
            # {
            #     'type': '10',  # 企业联系人人脸活检结果;
            #     'dataType': '',
            #     'data': '',
            # },
            {
                'type': '11',  # 实际经营地址; 必填;
                'dataType': '1',
                'data': '1',
            },
            {
                'type': '12',  # 实际经营地址材料（租赁合同或房产证书）;
                'dataType': '1',
                'data': '1',
            }
        ],
        # 股东信息列表: 至少1条，最多10条;
        'shareholders': [
            {
                'name': '股东1',  # 股东姓名;
                'contributeType': '01',
                # 出资方式: 01-资金(资本构成) , 02-技术(资本构成) , 03-实物(资本构成) , 04-权利(资本构成) , 05-其他(资本构成);
                'contributeProportion': '1',  # 出资比例: 单位：%,不上送百分号, 大于0小于等于100;
                'jobTitle': 'CEO1',  # 职务;
            },
        ],
        # 受益人信息列表: 至少1条，最多10条;
        'beneficiary': [
            {
                'name': '受益人1',  # 受益人姓名;
                'connectPhone': '18664388001',  # 受益人联系电话;
            },
        ]
    }
    r = A01.execute_api_request(data=data)
    logger.info(f"接口返回报文：{r.text}")
    assert r.status_code == 200

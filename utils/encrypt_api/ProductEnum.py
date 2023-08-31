# -#- coding: utf-8 -#-
# @Time    : 2022/11/11 17:14
# @Author  : linwei

from enum import Enum


class ProductEnum(Enum):
    # 企业注册入网
    ENTERPRISE_REGISTER = ["A01", "/enterprise/register"]

    # 企业注册结果查询
    ENTERPRISE_REGISTER_QUERY = ["A02", "/enterprise/register/query/result"]

    # 银行卡注册申请
    BANK_CARD_REGISTER_APPLY = ["A03", "/bank/card/register"]

    # 银行卡注册申请结果查询
    BANK_CARD_REGISTER_APPLY_QUERY = ["A04", "/bank/card/register/query"]

    # 企业信息修改申请
    ENTERPRISE_MODIFY_APPLY = ["A05", "/enterprise/modify/apply"]

    # 企业信息修改申请结果查询
    ENTERPRISE_MODIFY_QUERY = ["A06", "/enterprise/modify/query"]

    # 企业查余
    ENTERPRISE_BALANCE = ["A07", "/enterprise/query/balance"]

    # 企业信息
    ENTERPRISE_INFO = ["A08", "/enterprise/query/info"]

    # 网关充值订单创建申请
    WEB_RECHARGE_CREATE_ORDER_APPLY = ["B01", "/web/recharge/pre/create"]

    # 网关充值订单结果查询
    WEB_RECHARGE_ORDER_QUERY = ["B02", "/web/recharge/query/status"]

    # 企业网银转账充值
    TRANSFER_RECHARGE_SUPPORT_BANK_QUERY = ["C01", "/transfer/recharge/support/bank/query"]

    # 订单创建申请
    ORDER_CREATE_APPLY = ["D01", "/order/place/batch"]

    # 订单信息查询
    ORDER_QUERY = ["D02", "/order/query"]

    # 支付订单创建申请
    PAY_ORDER_CREATE_APPLY = ["D03", "/pay/order/create"]

    # 支付订单信息查询
    PAY_ORDER_QUERY = ["D04", "/pay/order/query/status"]

    # 卖方确认发货
    ORDER_SELLER_CONFIRM = ["D05", "/order/seller/confirm/shipped"]

    # 买方确认签收
    ORDER_BUYER_CONFIRM = ["D06", "/order/buyer/confirm/reception"]

    # 平台确认订单
    ORDER_PLATFORM_CONFIRM = ["D07", "/order/platform/confirm"]

    # 企业提现申请
    WITHDRAW_CREATE = ["E01", "/withdraw/create"]

    # 企业提现结果查询
    WITHDRAW_QUERY = ["E02", "/withdraw/query/status"]

    # 交易凭证申请
    VOUCHER_APPLY = ["V01", "/voucher/apply"]

    # 交易凭证查询
    VOUCHER_QUERY = ["V02", "/voucher/query"]

    # 短信发送
    SMS_SEND = ["H01", "/sms/send"]

    # 短信发送状态查询
    SMS_SEND_QUERY = ["H02", "/sms/query"]

    # 企业四要素认证
    ENTERPRISE_FOUR_ELEMENT_VERIFY = ["F03", "/enterprise/verify/four/element"]

    # 企业四要素认证结果查询
    ENTERPRISE_FOUR_ELEMENT_VERIFY_QUERY = ["F04", "/enterprise/verify/four/element/query"]

    # 银行卡三要素认证
    BANK_CARD_THREE_ELEMENT_VERIFY = ["F05", "/bank/card/verify/three/element"]

    # 银行卡三要素认证结果查询
    BANK_CARD_THREE_ELEMENT_VERIFY_QUERY = ["F06", "/bank/card/verify/three/element/query"]

    # 小额鉴权
    SMALL_AMOUNT_AUTH = ["F07", "/small/amount/auth"]

    # 小额鉴权结果查询
    QUERY_SMALL_AMOUNT_AUTH = ["F08", "/small/amount/auth/query/status"]

    # 承信兑付创建
    CREDIT_CREATE = ["J01", "/credit/order/create"]

    # 承信兑付信息查询
    CREDIT_QUERY_INFO = ["J02", "/credit/order/query/info"]

    # 取消兑付申请
    CREDIT_CANCEL = ["J03", "/credit/order/cancel"]

    # 开通核心企业
    OPEN_NUCLEUS_ENTERPRISE = ["J04", "/enterprise/nucleus/open"]


if __name__ == '__main__':
    res = ProductEnum.ENTERPRISE_REGISTER_QUERY.value
    print(res)
    res = ProductEnum.ENTERPRISE_REGISTER_QUERY.value[0]
    print(res)
    res = ProductEnum.ENTERPRISE_REGISTER_QUERY.value[1]
    print(res)

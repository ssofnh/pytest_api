# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 17:18
# @Author  : linwei


import pyDes
import base64


def pgt_encrypt(data):
    key = "bestpay.000"  # 密钥,一般是8位或16位
    # key = "kkk11111"  # 加密key,加密方式ECB秘钥必须是八位字节
    # mode = pyDes.ECB  # 加密方式 默认是ECB,也可以不填写
    # IV = "00000000"  # 偏移量,加密方式不是ECB的时候加密key字段必须是16位字节,秘钥不够用0补充
    k = pyDes.des(key[:-3], pad=None, padmode=pyDes.PAD_PKCS5)  # 传入秘钥,加密方式
    d = k.encrypt(data.encode("utf-8"))  # 加密数据
    base = str(base64.b64encode(d), encoding="utf-8")  # 指定输出格式为base64
    print(base)
    return base


def pgt_decrypt(data):
    key = "bestpay.000"
    des_obj = pyDes.des(key[:-3], pad=None, padmode=pyDes.PAD_PKCS5)
    decodebs64data = base64.b64decode(data)
    res = des_obj.decrypt(decodebs64data).decode('utf-8')
    print(res)
    return res


if __name__ == '__main__':
    # 加密
    pgt_encrypt('天津金融资产登记结算有限公司')
    # 解密
    pgt_decrypt('8I2bbvLJUrgd9LJFPZymFQ==')


# -*- coding: utf-8 -*-
# @Time    : 2023/1/29 14:38
# @Author  : linwei


import hashlib


def MD5_32_small(text='64042219850811657X'):
    res = hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()
    # print(res)
    return res


# print(MD5_32_small('93640105886064969L01123456'))

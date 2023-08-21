# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 10:14
# @Author  : linwei

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

key = "0CoJUm6Qyw8W8jub"
iv = "DYgjCEIMVrj2W9xM"


class Aes_cbc_encrypt_decrypt:

    def pkcs7padding(self, data, block_size=16):
        data = data.encode()
        if type(data) != bytearray and type(data) != bytes:
            raise TypeError("仅支持 bytearray/bytes 类型!")
        pl = block_size - (len(data) % block_size)
        return data + bytearray([pl for i in range(pl)])

    # 加密函数
    def encrypt(self, text, key=key, iv=iv):
        key = key.encode('utf-8')
        iv = iv.encode()
        mode = AES.MODE_CBC
        text = self.pkcs7padding(text)
        cryptos = AES.new(key, mode, iv)
        cipher_text = cryptos.encrypt(text)
        # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        return b2a_hex(cipher_text).decode()

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text, key=key, iv=iv):
        key = key.encode('utf-8')
        iv = iv.encode()
        mode = AES.MODE_CBC
        cryptos = AES.new(key, mode, iv)
        plain_text = cryptos.decrypt(a2b_hex(text))
        return plain_text[:-int(plain_text[-1])].decode()


if __name__ == '__main__':
    text1 = "13544156710"  # 待加密明文
    text2 = "AB936105FCBD6A88774A2E100C8C45B7"  # 待解密

    e = Aes_cbc_encrypt_decrypt().encrypt(text=text1)  # 加密
    d = Aes_cbc_encrypt_decrypt().decrypt(text=text2)  # 解密
    print("加密:", e)
    print("解密:", d)


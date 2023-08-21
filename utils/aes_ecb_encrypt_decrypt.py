# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 13:55
# @Author  : linwei

from Crypto.Util.Padding import pad
import base64
from base64 import b64decode, b64encode
from Crypto.Cipher import AES

key = "12345678ASDFGHJK"

# 去除补位
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def aes_encrypt(aes_str):
    # 使用key,选择加密方式
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')  # 选择pkcs7补全
    encrypt_aes = aes.encrypt(pad_pkcs7)
    # 加密结果
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 解码
    encrypted_text_str = encrypted_text.replace("\n", "")
    # 此处我的输出结果老有换行符，所以用了临时方法将它剔除
    return encrypted_text_str


def aes_decrypt(text):
    """
    解密 ：偏移量为key[0:16]；先base64解，再AES解密，后取消补位
    :param encrypted_text : 已经加密的密文
    :return:
    """
    encrypted_text = b64decode(text)
    cipher = AES.new(key=key.encode('utf-8'), mode=AES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    return unpad(decrypted_text).decode('utf-8')




if __name__ == '__main__':
    # key的长度需要补长(16倍数),补全方式根据情况而定,此处我就手动以‘0’的方式补全的32位key
    # key字符长度决定加密结果,长度16：加密结果AES(128),长度32：结果就是AES(256)
    # key = "".join(random.sample("0123efghjkl456mnopqstuvwsz789abcdef", 16))
    # 加密字符串长同样需要16倍数：需注意,不过代码中pad()方法里，帮助实现了补全（补全方式就是pkcs7）
    aes_str = '15199105927'
    # 加密
    encryption_result = aes_encrypt(aes_str)
    print(encryption_result)
    # 解密
    text = "sAbnxgcPLOwAS+hoZ1EOzg=="
    decrypt_result = aes_decrypt(text)
    print(decrypt_result)


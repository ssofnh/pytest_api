# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 15:17
# @Author  : linwei

from config.file_path_config import ACCESS_TOKEN_PATH
import os



class ReadWriteFile:
    def __init__(self, filepath='', filename=''):
        '''
        :param filename: 文件名字
        :param filepath: 写入指定目录
        '''
        self.filepath = filepath
        self.filename = filename

    def dirname(self):
        '''
        :param fileName: 文件名字
        :param filepath: 写入指定目录
        :return:
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), self.filepath, self.filename)

    def write_file(self, text):
        '''写入文件'''
        with open(self.dirname(), 'w') as f:
            return f.write(text)

    def read_file(self):
        '''读取文件'''
        with open(self.dirname(), 'r') as f:
            return f.read()


if __name__ == '__main__':
    text = '666'
    # 写入token
    ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_sys_token.md').write_file(text)
    ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_sys_api_token.md').write_file(text)
    ReadWriteFile(ACCESS_TOKEN_PATH, 'account_book_token.md').write_file(text)
    ReadWriteFile(ACCESS_TOKEN_PATH, 'account_book_api_token.md').write_file(text)
    ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_enterprise_token.md').write_file(text)
    # 读取token
    hthl_sys_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_sys_token.md').read_file()
    hthl_sys_api_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_sys_api_token.md').read_file()
    account_book_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'account_book_token.md').read_file()
    account_book_api_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'account_book_api_token.md').read_file()
    hthl_enterprise_token = ReadWriteFile(ACCESS_TOKEN_PATH, 'hthl_enterprise_token.md').read_file()

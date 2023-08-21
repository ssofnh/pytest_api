# -*- coding: utf-8 -*-
# @Time    : 2023/4/14 17:58
# @Author  : linwei


import requests

from config.file_path_config import ACCESS_TOKEN_PATH
from utils.ReadWriteFile_Helper import ReadWriteFile


class execute_get_token():

    def __init__(self, auto_setToken=None):
        self.auto_setToken = auto_setToken

    def hthl_sys_get_token(self, username='linwei', password='123456'):
        '''恒天管理系统--后台token'''
        url = self.auto_setToken.get('hthl_sys_get_token')
        # print(url)
        headers = {"Authorization": "Basic dGVzdDp0ZXN0"}
        params = {"grant_type": "password", "scope": "server"}
        data = {"username": username, "password": password}
        try:
            res = requests.post(url=url, data=data, params=params, headers=headers, verify=False, timeout=2)
            # print("hthl_sys_get_token:", res.text)
            hthl_sys_token = res.json().get('access_token')
            return hthl_sys_token
        except:
            return None

    def hthl_sys_api_get_token(self, username='linwei', password='123456'):
        '''恒天管理系统--接口token'''
        url = self.auto_setToken.get('hthl_sys_api_get_token')
        headers = {"Authorization": "Basic dGVzdDp0ZXN0"}
        params = {"grant_type": "password", "scope": "server"}
        data = {"username": username, "password": password}
        try:
            res = requests.post(url=url, data=data, params=params, headers=headers, verify=False, timeout=2)
            # print("hthl_sys_api_get_token:", res.text)
            hthl_sys_api_token = res.json().get('access_token')
            return hthl_sys_api_token
        except:
            return None

    def account_book_get_token(self, username='linwei', password='123456'):
        '''智能账簿管理系统--后台token'''
        url = self.auto_setToken.get('account_book_get_token')
        headers = {'Authorization': 'Basic dGVzdDp0ZXN0', 'Content-Type': 'application/x-www-form-urlencoded'}
        params = (
            ('username', username),
            ('password', password),
            ('grant_type', 'password'),
            ('scope', 'server'),
        )
        try:
            res = requests.post(url=url, params=params, headers=headers, verify=False, timeout=2)
            # print("account_book_get_token:", res.text)
            account_book_token = res.json().get('access_token')
            return account_book_token
        except:
            return None

    def account_book_api_get_token(self):
        '''智能账簿管理系统--接口token'''
        url = self.auto_setToken.get('account_book_api_get_token')
        headers = {'Authorization': 'Basic aHRibXM6aHRibXM=',
                   'Content-Type': 'application/x-www-form-urlencoded'}  # dGVzdDp0ZXN0 aHRibXM6aHRibXM=
        params = (
            ('grant_type', 'client_credentials'),
            ('scope', 'server'),
        )
        try:
            res = requests.post(url=url, params=params, headers=headers, verify=False, timeout=2)
            # print("account_book_api_get_token:", res.text)
            account_book_api_token = res.json().get('access_token')
            return account_book_api_token
        except:
            return None

    def hthl_sys_enterprise_get_token(self, username, password='JFat0ZdcX3E='):
        '''恒天管理系统--企业前端--企业用户token'''
        url = self.auto_setToken.get('hthl_enterprise_api_get_token')
        headers = {"Authorization": "Basic ZW50X2NsaWVudDplbnRfY2xpZW50"}
        params = (
            ('grant_type', 'password'),
            ('scope', 'server'),
        )
        data = {"username": username, "password": password}
        try:
            res = requests.post(url=url, data=data, params=params, headers=headers, verify=False, timeout=2)
            if res.json().get('data') != 'invalid_exception' or res.json().get('msg') != '用户名不存在或者密码错误':
                hthl_sys_enterprise_token = res.json().get('access_token')
                return hthl_sys_enterprise_token
            else:
                return res.json()
        except:
            return None

    def inside_account_book_api_get_token(self):
        '''当前无效'''

        '''智能账簿管理系统--接口token'''
        url = self.auto_setToken.get('account_book_api_get_token')
        headers = {'Authorization': 'Basic aHRibXM6aHRibXM=',
                   'Content-Type': 'application/x-www-form-urlencoded'}  # dGVzdDp0ZXN0 aHRibXM6aHRibXM=
        params = (
            ('grant_type', 'client_credentials'),
            ('scope', 'server'),
        )
        try:
            res = requests.post(url=url, params=params, headers=headers, verify=False, timeout=2)
            # print("account_book_api_get_token:", res.text)
            inside_account_book_api_token = res.json().get('access_token')
            return inside_account_book_api_token
        except:
            return None


class auto_setTokens(execute_get_token):
    def get_token(self):
        '''将token写入文件，以便后续读取'''
        hthl_sys_token = self.hthl_sys_get_token()
        hthl_sys_api_token = self.hthl_sys_api_get_token()
        account_book_token = self.account_book_get_token()
        account_book_api_token = self.account_book_api_get_token()
        data_dict = {}
        if hthl_sys_token or hthl_sys_api_token or account_book_token or account_book_api_token:
            if hthl_sys_token:
                filename = 'hthl_sys_token.md'
                # 写入文件
                ReadWriteFile(ACCESS_TOKEN_PATH, filename).write_file(hthl_sys_token)
                # 读取文件
                hthl_sys_token_res = ReadWriteFile(ACCESS_TOKEN_PATH, filename).read_file()
                data_dict['hthl_sys_token_res'] = hthl_sys_token_res
                # print("19191919",data_dict)
            if hthl_sys_api_token:
                filename = 'hthl_sys_api_token.md'
                # 写入文件
                ReadWriteFile(ACCESS_TOKEN_PATH, filename).write_file(hthl_sys_api_token)
                # 读取文件
                hthl_sys_api_token_res = ReadWriteFile(ACCESS_TOKEN_PATH, filename).read_file()
                data_dict['hthl_sys_api_token_res'] = hthl_sys_api_token_res
                # print("252525",data_dict)
            if account_book_token:
                filename = 'account_book_token.md'
                # 写入文件
                ReadWriteFile(ACCESS_TOKEN_PATH, filename).write_file(account_book_token)
                # 读取文件
                account_book_token_res = ReadWriteFile(ACCESS_TOKEN_PATH, filename).read_file()
                data_dict['account_book_token_res'] = account_book_token_res
                # print("3131313",data_dict)
            if account_book_api_token:
                filename = 'account_book_api_token.md'
                # 写入文件
                ReadWriteFile(ACCESS_TOKEN_PATH, filename).write_file(account_book_api_token)
                # 读取文件
                account_book_api_token_res = ReadWriteFile(ACCESS_TOKEN_PATH, filename).read_file()
                data_dict['account_book_api_token_res'] = account_book_api_token_res
            # print("auto_setTokens:", data_dict)
        else:
            print('未写入成功，请检查参数是否有误！')


if __name__ == '__main__':
    print(auto_setTokens().get_token())
    # print(execute_get_token().hthl_sys_get_token())  # pass
    # print(execute_get_token().hthl_sys_api_get_token())
    # print(execute_get_token().account_book_get_token())  # pass
    # print(execute_get_token().account_book_api_get_token())
    # print(execute_get_token().hthl_sys_enterprise_get_token(username='13550109687'))
    pass

    # 读取token
    # hthl_sys_token = ReadWriteFile(ACCESS_TOKEN_PATH, filename='hthl_sys_token.md').read_file()
    # hthl_sys_api_token = ReadWriteFile(ACCESS_TOKEN_PATH, filename='hthl_sys_api_token.md').read_file()
    # account_book_token = ReadWriteFile(ACCESS_TOKEN_PATH, filename='account_book_token.md').read_file()
    # account_book_api_token = ReadWriteFile(ACCESS_TOKEN_PATH, filename='account_book_api_token.md').read_file()

    # data = {'size': 10, 'current': 1}
    # header = {'Content-Type': 'application/x-www-form-urlencoded'}
    # hthl_sys_token_headers = {'Authorization': 'Bearer ' + execute_get_token().hthl_sys_get_token()}
    # headers = {**header, **hthl_sys_token_headers}
    # r = requests.get(query_url.get('恒天管理系统')+'/web-center/enterprise/page?size=10&current=1', data=data,
    #                  headers=headers)
    # print(r.json())

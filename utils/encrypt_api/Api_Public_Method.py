# -#- coding: utf-8 -#-
# @Time    : 2022/11/11 17:14
# @Author  : linwei

import warnings

# action参数可以设置为ignore
warnings.filterwarnings(action='ignore')
import time, datetime, random, base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from utils.encrypt_api.ProductEnum import ProductEnum
from utils.encrypt_api.StringToDict import StringToDict


class Api_Public_Method():

    def __init__(self, type=None, x_platform_code=None, privateKey=None, x_product_code=None):
        # 请求接口类型
        self.type = type
        # 平台编号
        self.x_platform_code = x_platform_code
        # 客户端私钥
        self.privateKey = privateKey
        # 产品编号
        self.x_product_code = x_product_code

        # 当前时间：年月日时分秒
        self.YMDHMS = time.strftime('%Y%m%d%H%M%S')
        #  当前时间：年月日
        self.YMD = time.strftime('%Y%m%d')

    def process_request(self, data, timestamp):
        # 默认接口的处理
        send_data = False
        pairs_dict = self.map_data(mapdata=data)
        sign_data = self.get_sign_params(pairs_dict) + timestamp
        if self.type in [ProductEnum.ENTERPRISE_REGISTER] and data.get('connectPerson'):
            # 如果是A01接口的签名预处理
            send_data = self.A01_requests_data(requests_data=data)
            pairs_dict = self.A01_sign_data(sign_data=data)
            sign_data = self.get_sign_params(pairs_dict)
            sign_data = sign_data.replace(';', ', ').replace('&connectPerson=', '&connectPerson={').replace(
                ', &connectPhone', '}&connectPhone').replace(', &', '}&') + timestamp
        # 执行签名方法
        sign = self.rsa_sign(sign_data)
        return send_data, pairs_dict, sign

    def prepare_headers(self, sign, timestamp):
        headers = {
            'Content-Type': 'application/json',
            'x-sign': sign,
            'x-timestamp': timestamp,
            'x-platform-code': self.x_platform_code,
            'x-product-code': self.x_product_code,
        }
        return headers

    # def send_request(self, url, data, headers):
    #     try:
    #         response = requests.post(url, data=json.dumps(data, separators=(',', ':')), headers=headers, verify=False,
    #                                  timeout=60)
    #         return response.json()
    #
    #     except requests.exceptions.RequestException as e:
    #         print("请求异常:", e)
    #         return None
    #
    # def send_and_process_request(self, url, data, headers):
    #     start_time = datetime.datetime.now()
    #     print("请求发送时间：", start_time)
    #
    #     response_json = self.send_request(url, data, headers)
    #
    #     end_time = datetime.datetime.now()
    #     print("请求返回时间：", end_time)
    #     delta = end_time - start_time
    #     total_seconds = delta.total_seconds()
    #     milliseconds = int(delta.total_seconds() * 1000)
    #     print(f"请求时间差: {total_seconds:.3f}s ({milliseconds}ms)")
    #
    #     if response_json:
    #         print("返回报文：")
    #         pprint(response_json)
    #         return response_json

    def Interface_template(self, data=None):
        timestamp = str(int(time.time() * 1000))
        send_data, pairs_dict, sign = self.process_request(data, timestamp)
        headers = self.prepare_headers(sign, timestamp)
        # self.send_and_process_request(url=self.url, data=send_data if send_data else pairs_dict, headers=headers)
        return send_data, pairs_dict, headers

    def map_data(self, mapdata):
        # map排序
        sorted_obj = {i: mapdata[i] for i in sorted(mapdata.keys())}
        pairs_dict = StringToDict(sorted_obj)
        return pairs_dict

    @staticmethod
    def get_sign_params(params):
        # map排序
        sorted_obj = {k: v for k, v in sorted(params.items())}
        param_strings = [
            f'{k}={v if v and not isinstance(v, list) else str(v).replace(" ", "")}'
            for k, v in sorted_obj.items()
        ]
        return '&'.join(param_strings).replace('\'', "\"").replace(" ", "")

    def A01_requests_data(self, requests_data):
        # connectPerson参数排序
        connectPerson_requests_data = requests_data.get('connectPerson', {})
        sorted_connectPerson = {k: v for k, v in sorted(connectPerson_requests_data.items())}
        requests_data['connectPerson'] = sorted_connectPerson
        send_data = self.map_data(requests_data)
        return send_data

    def A01_sign_data(self, sign_data):
        # A01接口参数预处理
        connectPerson_sign_data = sign_data.get('connectPerson')
        keys = connectPerson_sign_data.keys()
        connectPerson_sign_data = {i: connectPerson_sign_data[i] for i in sorted(keys)}
        S = ''
        for k, v in connectPerson_sign_data.items():
            N = k + '=' + v + ','
            S += N
        S = S.replace(',', ';')
        sign_data['connectPerson'] = S
        pairs_dict = self.map_data(mapdata=sign_data)
        return pairs_dict

    def rsa_sign(self, data):
        # 加密请求报文
        private_keyBytes = base64.b64decode(str(self.privateKey))
        priKey = RSA.importKey(private_keyBytes)
        signer = PKCS1_v1_5.new(priKey)
        hash_obj = SHA256.new(data.encode('utf-8'))
        signature = base64.b64encode(signer.sign(hash_obj))
        return signature

    def clientOrderNo(self):
        """
        :return: 20220525140635467912
        :PS ：并发较高时尾部随机数增加
        """
        clientOrderNo = str(datetime.datetime.fromtimestamp(time.time())).replace("-", "").replace(" ", "").replace(":",
                                                                                                                    "").replace(
            ".", "") + str(random.randint(100, 999))
        return clientOrderNo


if __name__ == '__main__':
    pass
    print(Api_Public_Method().clientOrderNo())

# -*- coding: utf-8 -*-
# @Time    : 2022/11/18 15:01
# @Author  : linwei

import json


class StringToDict(dict):

    def __str__(self):  # 显示对象的字符串形式
        return json.dumps(self, ensure_ascii=False).replace(" ", "")

    # def __repr__(self): # 显示对象属性
    #     print('my name is {}'.format(self.keys()))
    #     return 'haha' # 不写return语句，会隐式执行return语句

# if __name__ == '__main__':
#     pairs = {'connectPerson': {'idValidityTimeEnd': '', 'idFrontPhoto': '',}}
#     pairs_dict = mydict(pairs)
#     print(type(pairs),pairs_dict) # <class 'dict'> {"arun": "maya", "bill": "samantha", "jack": "ilena", "hari": "aradhana"}


# python 调用java
# import jpype,os,demjson3,json,time
# from jpype import *
#
# base_dir = os.path.dirname(os.path.realpath(__file__))
#
# class Channel_Base():
#
#     def startJVM(self,jarpath,dependency):
#         '''
#
#         :param jarpath: jar包路径
#         :param dependency: 引用包路径
#         :return:
#         '''
#         # 启动jvm
#         if jpype.isJVMStarted() == False:
#             startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" %jarpath,"-Djava.ext.dirs=%s" %dependency)
#
#             if jpype.isJVMStarted() == True:
#                 print('startJVM success!')
#             if jpype.isJVMStarted() == False:
#                 print('startJVM fail!')
#         else:
#             print('startJVM all ready!')
#
#     def shutdownJVM(self):
#         #关闭JVM
#         # print('shutdownJVM1111')
#         # print(jpype.isJVMStarted())
#         jpype.shutdownJVM()
#         # print('shutdownJVM22322')
#         # print(jpype.isJVMStarted())
#
#
#     def JSON_toJSONString(self,str_obj):
#         '''将java返回的字符串对象转换成python的字典格式'''
#         # 1.找到类；
#         self.JSON = JClass("com.alibaba.fastjson.JSON")
#         # 2.静态方法：不实例化对象使用；将java对象转换成json格式；
#         res = self.JSON.toJSONString(str_obj,jpype.JInt())
#         # 3.将java的不规则JSON格式转换成python的字典格式。
#         res = demjson3.decode(str(res))
#         print(json.dumps(res,indent=3,ensure_ascii=False))
#         return res

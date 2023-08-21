# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 9:53
# @Author  : linwei


class Max_Page_Number():

    def total_size(self,total, size):
        '''
        计算最大的页码
        :param total: 总条数  int(str)
        :param size: 每页显示条数 int(str)
        :return: 最大页码
        '''
        total = int(total)
        size = int(size)
        if total % size == 0:
            return total // size
        else:
            return total // size + 1

if __name__ == '__main__':
    res = Max_Page_Number().total_size(total=89, size=10)
    print(res)


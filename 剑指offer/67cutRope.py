# -*- coding:utf-8 -*-
"""
剪绳子
2 = 1*1
3 = 1*2
4 = 2*2
5 = 2*3
6 = 3*3
.
.
.
从序列中可以看出当n为4时拆成两个的乘积刚好等于4，
当n小于4，拆成两个的乘积结果小于n。所以2和3是最小的拆解单位。
当n大于4后，拆成两个的乘积结果会大于n。
"""


class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        if number == 3:
            return 2
        numOf2 = number % 3
        if numOf2 == 1:
            numOf3 = (number - 4) // 3
            return 2 * 2 * (3 ** numOf3)
        else:
            numOf3 = (number - 2) // 3
            return 2 * (3 ** numOf3)

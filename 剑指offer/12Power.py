"""
题目：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
思路：快速幂算法
考虑案例：exponent是奇数偶数负数的情况
如果exponent是负数，则取正后再返回倒数；
假设exponent是正数，有奇数偶数两种情况
如果为偶数，那么Power(res, exponent) = Power(res, exponent//2)**2
如果为奇数的话，还要在偶数的结果基础上再乘上一个base
"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        flag = 0
        if exponent < 0:
            flag = 1
            exponent = -exponent
        halfRes = self.Power(base, exponent >> 1)
        res = halfRes ** 2
        if exponent & 1 == 1:
            res *= base
        return res if flag == 0 else 1 / res

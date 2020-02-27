"""
29 两数相除（中等）
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，
要求不使用乘法、除法和 mod 运算符。

思路：找出尽可能大的n： 被除数/2^n>=除数
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        MINVALUE = -2 ** 31
        if dividend == MINVALUE and divisor == -1:
            return -(MINVALUE + 1)
        negative = dividend ^ divisor < 0
        total = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        for i in range(31, -1, -1):
            if dividend >> i >= divisor:
                total += 1 << i
                dividend -= divisor << i

        return -total if negative else total

"""
二进制中1的个数：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
思路：数字每次跟1做位与后，右移直到数字为0
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = n & 1
        for i in range(1, 32):
            n = n >> 1
            count += n & 1
        return count

"""
67 二进制求和（简单）

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"


"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        位数补齐，按位相加
        """
        alen, blen = len(a), len(b)
        lens = max(alen, blen)
        a = '0' * (lens - alen) + a
        b = '0' * (lens - blen) + b
        res = ''
        carry = 0
        for i in range(lens - 1, -1, -1):
            digit = int(a[i]) + int(b[i]) + carry
            carry = digit // 2
            digit = digit % 2
            res = str(digit) + res
        if carry == 1:
            res = '1' + res
        return res


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        位运算
        """
        a, b = int(a, 2), int(b, 2)
        while b:
            xor = a ^ b
            carry = (a & b) << 1
            a = xor
            b = carry
        return bin(a)[2:]

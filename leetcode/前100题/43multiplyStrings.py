"""
43 字符串相乘（中等）
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = ''
        levelCarry = 0
        for j in range(len(num2) - 1, -1, -1):
            d2 = ord(num2[j]) - ord('0')
            total = 0
            carry = 0
            count = 1
            # 逐个相乘
            for i in range(len(num1) - 1, -1, -1):
                d1 = ord(num1[i]) - ord('0')
                prod = d1 * d2 + carry
                carry = prod // 10
                total = total + (prod % 10) * count
                count *= 10
            if carry != 0:
                total += carry * count
            total += levelCarry
            res = '%d' % (total % 10) + res
            levelCarry = total // 10
        if levelCarry != 0:
            res = '%d' % levelCarry + res
        return res

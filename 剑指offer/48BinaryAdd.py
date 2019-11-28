# -*- coding:utf-8 -*-
"""
计算不进位的数值
计算进位，与+左移一位。
当没有进位的时候就返回异或的值
"""


class Solution:
    def Add(self, num1, num2):
        # write code here
        while True:
            xor = num1 ^ num2
            andOp = (num1 & num2) << 1
            if andOp == 0:
                break
            else:
                num1 = xor
                num2 = andOp
        return xor


if __name__ == '__main__':
    s = Solution()
    print(s.Add(7, 30))

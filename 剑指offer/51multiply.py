# -*- coding:utf-8 -*-
"""
构建乘积数组
思路1：双重循环，到i的时候A[i]不要乘进去
思路2：将乘积看成两部分分开乘。

"""


class Solution:
    def multiply(self, A):
        # write code here
        B = [1]
        for item in A[:len(A) - 1]:
            B.append(B[-1] * item)
        acc = 1
        for index in range(len(A) - 1, -1, -1):
            B[index] *= acc
            acc *= A[index]
        return B

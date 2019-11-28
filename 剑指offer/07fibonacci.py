# -*- coding:utf-8 -*-
"""
斐波那契数列：f(n+1) = f(n)+f(n-1)
"""


class Solution:
    """
    0,1,1,2,3,5...
    """

    def Fibonacci(self, n):
        if n < 2:
            return n
        pre = 0
        current = 1
        for i in range(n - 1):
            nexti = pre + current
            pre = current
            current = nexti
        # write code here
        return current

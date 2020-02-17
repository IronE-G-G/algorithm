"""
50 pow(x,n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

思路：递归
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
        n = abs(n)

        def helper(x, n):
            if n == 1:
                return x
            if n % 2 == 0:
                return helper(x, n // 2) ** 2
            if n % 2 == 1:
                return x * helper(x, n // 2) ** 2

        res = helper(x, n)
        return res

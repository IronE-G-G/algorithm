"""
69 sqrt(x)（简单）
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        binary search
        """
        if x < 0:
            return None
        if x == 0:
            return 0
        if x <= 3:
            return 1
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

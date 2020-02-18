"""
70 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre = 1
        now = 2
        nextFloor = -1
        for i in range(3, n + 1):
            nextFloor = pre + now
            pre = now
            now = nextFloor
        return nextFloor

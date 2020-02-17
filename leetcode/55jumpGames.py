"""
55 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        maxpos记录每次起跳的最远距离
        begin，end记录下一次可以作为起跳点的元素区间

        """
        begin = 0
        end = 0
        maxPos = 0
        n = len(nums)
        while begin <= end:
            for i in range(begin, end + 1):
                maxPos = max(maxPos, nums[i] + i)
            if maxPos >= n - 1:
                return True
            begin = end + 1
            end = maxPos
        return False


class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1. dp
        状态：dpi为数组第i个元素是否能到达最后一个位置
        转移：
        从后往前遍历数组：
        if i+nums[i]>=n-1 ==> True
        elif begin = i+1,end = i+num[i]
        [begin,end]之间如果有dp元素为True，则dp[i] = True

        该算法在leetcode上那个最大的案例时间超出限制
        """
        n = len(nums)
        if n <= 1:
            return True
        dp = [False for _ in range(n)]
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= n - 1:
                dp[i] = True
            else:
                begin = i + 1
                end = i + nums[i]
                for index in range(begin, end + 1):
                    if dp[index]:
                        dp[i] = True
                        break
        return dp[0]

"""
41 缺失的第一个正数（困难）
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

思路：一个萝卜一个坑，把0<value<=n的放在value-1的位置
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            value = nums[i]
            if 0 < value <= n and value != i + 1 and nums[value - 1] != value:
                nums[i], nums[value - 1] = nums[value - 1], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

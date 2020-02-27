"""
全排列（中等）
给定一个没有重复数字的序列，返回其所有可能的全排列。
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(nums, path):
            if len(nums) == 1:
                res.append(path + nums)
                return
            for i in range(len(nums)):
                helper(nums[:i] + nums[(i + 1):], path + [nums[i]])

        helper(nums, [])
        return res

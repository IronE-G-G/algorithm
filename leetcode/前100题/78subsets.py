"""
78 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

思路：迭代，回溯
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        迭代
        """
        if not nums:
            return [[]]
        nums.sort()
        paths = [[], [nums[0]]]
        for i in range(1, len(nums)):
            newPaths = [path + [nums[i]] for path in paths]
            paths = paths + newPaths
        return paths


class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        回溯

        """

        res = []
        lens = len(nums)
        nums.sort()

        def backtrack(nexti, path):
            # 没有下一个元素
            res.append(path)
            if nexti == lens:
                return
            # 有下一个元素
            for i in range(nexti, lens):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res

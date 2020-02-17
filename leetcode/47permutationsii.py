"""
47 全排列ii（中等）

给定一个可包含重复数字的序列，返回所有不重复的全排列。

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def backtrack(nums, path):
            if len(nums) == 1:
                res.append(path + [nums[0]])
            for i in range(len(nums)):
                # 去重
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[(i + 1):], path + [nums[i]])

        backtrack(nums, [])
        return res

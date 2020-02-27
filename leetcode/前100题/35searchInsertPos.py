"""
35 搜索插入位置（简单）
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
假设无重复元素
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        lens = len(nums)
        left, right = 0, lens - 1
        while left <= right:
            mid = (left + right) // 2
            midValue = nums[mid]
            if midValue == target:
                return mid
            elif midValue > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

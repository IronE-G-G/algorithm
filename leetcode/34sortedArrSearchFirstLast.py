"""
34 在排序数组中查找元素的第一个和最后一个位置（中等）

"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        target1 = target - 0.5
        target2 = target + 0.5
        left = self.binarySearch(nums, target1)
        right = self.binarySearch(nums, target2)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def binarySearch(self, nums, target):
        lens = len(nums)
        left, right = 0, lens - 1
        while left <= right:
            mid = (left + right) // 2
            midValue = nums[mid]
            if midValue > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = self.leftBinarySearch(nums, target)
        right = self.rightBinarySearch(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def leftBinarySearch(self, nums, target):
        # 返回第一个大于等于target的坐标
        lens = len(nums)
        left, right = 0, lens
        while left < right:
            mid = (left + right) // 2
            midValue = nums[mid]
            if midValue == target:
                right = mid
            elif midValue < target:
                left = mid + 1
            else:
                right = mid
        return left

    def rightBinarySearch(self, nums, target):
        # 返回第一个大于target的坐标
        lens = len(nums)
        left, right = 0, lens
        while left < right:
            mid = (left + right) // 2
            midValue = nums[mid]
            if midValue <= target:
                left = mid + 1
            else:
                right = mid
        return right

"""
26 删除排序数组中的重复项（简单）

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，
返回移除后数组的新长度。
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        count = 1
        for ind in range(len(nums) - 2, -1, -1):
            if nums[ind] != nums[ind + 1]:
                count += 1
            else:
                nums.pop(ind)
        return count

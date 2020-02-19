"""
80 删除排序数组中的重复项

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        hash
        """
        counter = dict()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in counter:
                counter[nums[i]] = 1
            else:
                if counter[nums[i]] == 2:
                    nums.pop(i)
                else:
                    counter[nums[i]] += 1


class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return
        left = 0
        while True:
            if left + 2 >= len(nums):
                break
            else:
                if nums[left] == nums[left + 2]:
                    nums.pop(left)
                else:
                    left += 1
        return




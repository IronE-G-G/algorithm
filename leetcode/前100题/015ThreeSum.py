"""
三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

思路：排序，从左到右遍历数组，遍历元素作为最小的元素，双指针查找满足条件的其他两个元素。
去重：包括两部分，
1 从左到右遍历的时候去重；
2 找到满足条件的两个元素后，继续移动start指针，此时start指针的数必须跟之前的不一样。
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1 暴力 On3
        2 先排序，固定最小的一个，双指针找右边两个数之和等于最小的一个 On2
        """
        nums.sort()
        begin = 0
        res = []
        while begin < len(nums) - 2 and nums[begin] <= 0:
            if begin > 0 and nums[begin] == nums[begin - 1]:
                begin += 1
                continue
            left, right = begin + 1, len(nums) - 1
            while left < right:
                if left > begin + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if nums[left] + nums[right] == -nums[begin]:
                    res.append([nums[begin], nums[left], nums[right]])
                    left += 1
                elif nums[left] + nums[right] > -nums[begin]:
                    right -= 1
                else:
                    left += 1
            begin += 1
        return res




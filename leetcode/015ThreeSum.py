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
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        length = len(nums)
        for ind in range(length):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            else:
                start, end = ind + 1, length - 1
                while start < end:
                    sum3 = nums[ind] + nums[start] + nums[end]
                    if sum3 == 0:
                        res.append([nums[ind], nums[start], nums[end]])
                        start += 1
                        # 对start进行去重
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                    elif sum3 > 0:
                        end -= 1
                    else:
                        start += 1
        return res

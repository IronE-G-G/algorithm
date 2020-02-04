"""
31 下一个排列

从后往前扫描，发现位置i比位置i+1小，从i+1开始的后半段中找到比位置i大的最小数跟位置i交换，
对i+1开始的后半段进行排序

"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        N = len(nums)
        flag = False
        for index in range(N - 2, -1, -1):
            if nums[index] < nums[index + 1]:
                min_value = nums[index + 1]
                min_pos = index + 1
                for i in range(index + 2, N):
                    if nums[index] < nums[i] < min_value:
                        min_value = nums[i]
                        min_pos = i
                nums[index], nums[min_pos] = nums[min_pos], nums[index]
                right_part = sorted(nums[index + 1:])
                nums[index + 1:] = right_part
                flag = True
                break
        if not flag:
            nums.sort()

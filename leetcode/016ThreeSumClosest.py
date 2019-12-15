"""
最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案

思路：排序+双指针，思路跟三数之和差不多，而且不用判断去重

"""


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) < 3:
            return None
        res = None
        gap = None
        length = len(nums)
        nums.sort()
        for ind in range(length):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            start, end = ind + 1, length - 1
            while start < end:
                current_gap = nums[ind] + nums[start] + nums[end] - target
                if gap is None or abs(current_gap) < gap:
                    gap = abs(current_gap)
                    res = current_gap + target

                if current_gap == 0:
                    return target
                elif current_gap > 0:
                    end -= 1
                else:
                    start += 1

        return res

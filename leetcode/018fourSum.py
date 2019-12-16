"""
四数之和
思路跟之前的三数之和是一样的还是用双指针，多了一层循环。
"""


class Solution:
    def fourSum(self, nums, target: int):
        length = len(nums)
        if length < 4:
            return []
        res = []
        nums.sort()
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                start, end = j + 1, length - 1
                while start < end:
                    candidate = [nums[i], nums[j], nums[start], nums[end]]
                    gap = sum(candidate) - target
                    if gap == 0:
                        res.append(candidate)
                        start += 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                    elif gap < 0:
                        start += 1
                    else:
                        end -= 1
        return res

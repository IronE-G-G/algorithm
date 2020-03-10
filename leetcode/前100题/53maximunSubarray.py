"""
53 最大子序列和（简单）
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

思路：dp
状态：dpi存储以第i个数组元素为结尾的最大子序列和
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        1 暴力 On3 On2
        2 dp 以元素i为结尾的最大子序和，On 空间复杂度压缩一下,以前一个元素为结尾的最大子序列和
        """
        pre = nums[0]
        res = pre
        for i in range(1, len(nums)):
            pre = max(pre, 0) + nums[i]
            res = max(pre, res)
        return res

# -*- coding:utf-8 -*-
"""
连续子数组的最大和
思路：动态规划，dpi保存arr[:(i+1)]中包含arr[i]的最大子序列和
"""


class Solution:

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [array[0]]
        res = array[0]
        for ind, item in enumerate(array[1:]):
            if dp[ind] < 0:
                tmp = item
            else:
                tmp = dp[ind] + item
            dp.append(tmp)
            res = max(res, tmp)
        return res

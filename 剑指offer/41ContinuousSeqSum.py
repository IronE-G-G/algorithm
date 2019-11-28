# -*- coding:utf-8 -*-
"""
面试题41 所有和为S的连续正数序列
思路：用两个指针指定序列范围。如果序列和大于tsum，则low往前移动，如果小，则high往前移动。
如果相等，加入res中，然后low和high都往前移动
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        low = 1
        high = 1
        currentSum = 1
        result = []
        while low <= tsum // 2:
            if currentSum < tsum:
                high += 1
                currentSum += high
            elif currentSum > tsum:
                currentSum -= low
                low += 1
            else:
                result.append(list(range(low, high + 1)))
                high += 1
                currentSum = currentSum - low + high
                low += 1
        return result

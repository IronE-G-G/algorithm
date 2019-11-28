"""
扑克牌顺子，给5张牌，检查是否连续，大王小王算0，可以代替其他值，A：1，JQK：11 12 13
1 2 3 4 5 算连续
思路：检查大小王个数，检查每个非零数不能重复，检查非零数的大小数间隔小于5
"""


# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) < 5:
            return False
        numSet = set()
        cnt0 = 0
        for num in numbers:
            if num == 0:
                cnt0 += 1
            elif num in numSet:
                return False
            else:
                numSet.add(num)
        numMin = min(numSet)
        numMax = max(numSet)
        if numMax - numMin < 5:
            return True
        return False

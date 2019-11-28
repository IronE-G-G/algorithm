"""
面试题41  两数之和
递增排序的数组和一个数字S,
在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

思路：使用两个指针从头尾开始，如果两指针指向的数字大于tsum，那么high指针往左边移动，如果小于，low指针移动
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, arr, tsum):
        # write code here
        lens = len(arr)
        low = 0
        high = lens-1
        while low<high:
            if arr[low]+arr[high]>tsum:
                high -= 1
            elif arr[low]+arr[high]<tsum:
                low +=1
            else:
                return [arr[low], arr[high]]
        return []

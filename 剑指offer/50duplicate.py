# -*- coding:utf-8 -*-
"""
数组中重复的字：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。

思路1：使用集合来收集只出现一次的元素
思路2：使用桶排序的思想；
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        unique = set()
        for ele in numbers:
            if ele in unique:
                duplication[0] = ele
                return True
            else:
                unique.add(ele)
        return False


class Solution2:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length = len(numbers)
        if length <= 1:
            return False
        index = 0
        while index < length:
            if numbers[index] == index:
                index += 1
            else:
                tmp = numbers[index]
                if numbers[tmp] == tmp:
                    duplication[0] = tmp
                    return True
                else:
                    numbers[index], numbers[tmp] = numbers[tmp], numbers[index]
        return False

# -*- coding:utf-8 -*-
"""
第一个只出现一次的字符
思路：使用一个集合来收集重复的字符，使用一个字典来收集字符出现的第一个位置。
对字符i，如果同时不在集合和字典中，则证明他是第一次出现。
遍历完后看字典中是否有存在元素，有则取最早进来的那个的位置。
"""
from collections import OrderedDict


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        unique_arr = OrderedDict()
        duplicate = set()
        for pos, char in enumerate(s):
            if char not in duplicate:
                if char not in unique_arr:
                    unique_arr[char] = pos
                else:
                    unique_arr.pop(char)
                    duplicate.add(char)
        return unique_arr.popitem(last=False)[1] if unique_arr else -1

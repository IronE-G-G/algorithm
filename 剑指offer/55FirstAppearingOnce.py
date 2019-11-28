# -*- coding:utf-8 -*-
"""
字符流中第一个不重复的字符
思路：用集合和字典分别记录重复的字符和第一次出现的字符的位置
"""


class Solution:
    # 返回对应char
    def __init__(self):
        self.collect = dict()
        self.cnt = 0
        self.duplicate = set()

    def FirstAppearingOnce(self):
        # write code here
        return sorted(self.collect.items(),
                      key=lambda x: x[1])[0][0] if self.collect else '#'

    def Insert(self, char):
        # write code here
        if char not in self.duplicate:
            if char not in self.collect:
                self.collect[char] = self.cnt
                self.cnt += 1
            else:
                self.collect.pop(char)
                self.duplicate.add(char)

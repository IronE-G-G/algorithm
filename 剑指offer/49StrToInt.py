# -*- coding:utf-8 -*-
"""
把字符串转化成整数

"""


class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        prefix = 1
        origin = 0
        if s[0] == '-':
            prefix = -1
        elif '0' < s[0] < '9':
            origin += (ord(s[0]) - ord('0'))
        for char in s[1:]:
            if '0' <= char <= '9':
                origin = origin * 10 + (ord(char) - ord('0'))
            else:
                return 0
        return origin * prefix

# -*- coding:utf-8 -*-
"""
左旋转字符串
思路1：python字符串拼接
思路2：将字符串划分成两部分，分别翻转，再整体翻转
"""


# -*- coding:utf-8 -*-
class Solution1:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]


class Solution2:
    def reverse(self, s, begin, end):
        while begin < end:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1

    def LeftRotateString(self, s, n):
        if not s or len(s) < n:
            return ''
        s = list(s)
        self.reverse(s, 0, n - 1)
        self.reverse(s, n, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
        return ''.join(s)

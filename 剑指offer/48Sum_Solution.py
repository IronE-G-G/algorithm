# -*- coding:utf-8 -*-
"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等
关键字及条件判断语句（A?B:C）。
剑指offer的234页有这道题的c++解法
"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n * (n + 1) / 2

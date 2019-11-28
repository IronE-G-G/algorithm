# -*- coding:utf-8 -*-
"""
包含min函数的栈：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
思路：维护最小值，push的时候把最小值也一起push进去。
"""
import sys


class Solution:
    minValue = sys.maxsize
    stack = []

    def push(self, node):
        # write code here
        if node < self.minValue:
            self.minValue = node
        self.stack.append(node)
        self.stack.append(self.minValue)

    def pop(self):
        # write code here
        self.stack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-2]

    def min(self):
        # write code here
        return self.stack[-1]

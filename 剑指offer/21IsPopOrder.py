"""
栈的压入弹出序列：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
思路：用一个栈来模拟序列压入弹出过程。
"""

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for item in popV:
            if stack and stack[-1] == item:
                stack.pop()
            else:
                while pushV:
                    candidate = pushV.pop(0)
                    if candidate != item:
                        stack.append(candidate)
                    else:
                        break
        return len(stack) == 0
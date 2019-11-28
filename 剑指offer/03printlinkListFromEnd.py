# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
从尾到头打印链表
思路1：加一个堆栈存放结点。
思路2：递归，打印第二个结点开始的链表再加上第一个结点。
"""


class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        return stack[::-1]


class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]

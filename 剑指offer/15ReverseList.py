# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
翻转链表：输入一个链表，反转链表后，输出新链表的表头。
思路：新增两个指针，cur负责将现结点指向前面结点组成的翻转链表，head是前面结点组成的翻转链表的表头。
pHead负责后面还没有翻转的结点。
"""


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        head = None
        cur = pHead
        while cur:
            pHead = pHead.next
            cur.next = head
            head = cur
            cur = pHead
        return head

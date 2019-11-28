"""
两个链表的第一个公共结点：输入两个链表，找出它们的第一个公共结点。
思路1：遍历一次各自记录长度，先走长的链表k（长度差）步，然后短的也一起走。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindLength(self, pHead):
        p = pHead
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        return cnt

    def FindFirstCommonNode(self, pHead1, pHead2):
        len1 = self.FindLength(pHead1)
        len2 = self.FindLength(pHead2)
        if len1 > len2:
            gap = len1 - len2
            for i in range(gap):
                pHead1 = pHead1.next
        elif len1 < len2:
            gap = len2 - len1
            for i in range(gap):
                pHead2 = pHead2.next
        while pHead1:
            if pHead1 == pHead2:
                break
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return pHead1

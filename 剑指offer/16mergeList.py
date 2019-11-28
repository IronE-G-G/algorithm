"""
合并两个排序链表
思路：新建一个head结点，新建一个cur结点指向head，cur负责将结点串起来。
分别比较两个链表的表头大小，cur的next指向小的表头结点，同时那个小的表头结点向后移动。
注意案例：两个链表长短不一样，两个链表存在空链表
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        head = ListNode(-1)
        cur = head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        elif pHead2:
            cur.next = pHead2
        return head.next

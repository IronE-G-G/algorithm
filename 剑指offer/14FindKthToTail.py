# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
链表中倒数第k个结点
思路：快慢指针，快的先走k步。
注意：k的值是否为0，是否不超过链表长度
"""


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        if k == 0:
            return None
        origin = head
        count = 1
        while count < k:
            if head.next:
                head = head.next
                count += 1
            else:
                return None
        while head.next:
            head = head.next
            origin = origin.next
        return origin

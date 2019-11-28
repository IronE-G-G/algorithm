# -*- coding:utf-8 -*-
"""
删除链表中重复的点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        origin_head = ListNode(-1)
        origin_head.next = pHead
        cur = pHead
        candidate = origin_head
        while cur and cur.next:
            # 如果节点重复，跳过重复的这些节点
            if cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                # 将下一个不跟前一位重复的节点列入参考
                candidate.next = cur
            else:
                # cur为不重复的节点
                candidate = cur
                cur = cur.next
        return origin_head.next

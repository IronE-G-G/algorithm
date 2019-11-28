"""
复杂链表的复制：
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
思路：
复制每一个元素并将复制的元素插入到原链表中；
添加random的指向；
将原链表和复制的链表拆开。

"""


# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        cur = pHead
        # 元素复制
        while cur:
            backupNode = RandomListNode(cur.label)
            temp = cur.next
            cur.next = backupNode
            backupNode.next = temp
            cur = temp
        # 添加random指向
        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分成两个链表
        cur2 = pHead.next
        curr = pHead
        while curr.next:
            tmp = curr.next
            curr.next = curr.next.next
            curr = tmp
        return cur2
        # write code here

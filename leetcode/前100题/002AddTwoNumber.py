# Definition for singly-linked list.
"""
两数相加
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

思路：遍历链表对每个位数进行相加
注意案例：两个链表长度不一样的情况；最后需要进位
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        cur = head
        flag = 0
        while l1 or l2:
            newValue = flag
            if l1:
                newValue += l1.val
                l1 = l1.next
            if l2:
                newValue += l2.val
                l2 = l2.next
            flag = newValue // 10
            newValue = newValue - flag * 10
            cur.next = ListNode(newValue)
            cur = cur.next
        if flag == 1:
            cur.next = ListNode(1)
        return head.next

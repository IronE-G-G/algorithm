"""
24 两两交换链表中的结点
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = ListNode(0)
        first.next = head
        p1 = first
        while p1.next and p1.next.next:
            p2 = p1.next
            p1.next = p2.next
            p2.next = p1.next.next
            p1.next.next = p2
            p1 = p2
        return first.next

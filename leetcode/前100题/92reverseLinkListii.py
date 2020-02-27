"""
92 翻转链表ii
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        翻转需要翻转的部分，再拼接
        """
        if not head or not head.next:
            return head
        res = ListNode(-1)
        res.next = head

        pre = res
        cur = head
        count = 1
        begin, end = cur, cur
        while count < n:
            tmp = cur
            cur = cur.next
            count += 1
            if count == m:
                begin = cur
                pre = tmp

        # reverse end
        behind = cur.next
        cur.next = None

        # join
        revBegin, revEnd = self.reverse(begin)
        pre.next = revBegin
        revEnd.next = behind
        return res.next

    def reverse(self, node):
        first = None
        last = node
        while node:
            behind = node.next
            node.next = first
            first = node
            node = behind
        return first, last

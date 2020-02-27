"""
83 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        遍历，如果更next相等，删除
        """
        if not head or not head.next:
            return head
        res = ListNode(-1)
        res.next = head
        pre = res
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return res.next

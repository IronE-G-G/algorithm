"""
82 删除排序链表中的重复元素ii （83 删除排序链表中的重复元素）
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        快慢指针

        """
        if not head or not head.next:
            return head
        res = ListNode(-1)
        res.next = head
        pre = res
        slow = head
        fast = head.next
        while fast:
            while fast and slow.val == fast.val:
                fast = fast.next
            # 需要跳过
            if slow.next != fast:
                # 重复的时候更新pre的next
                pre.next = fast
                slow = fast
                if fast:
                    fast = fast.next
            else:
                pre.next = slow
                pre = pre.next
                slow = fast
                fast = fast.next
        return res.next



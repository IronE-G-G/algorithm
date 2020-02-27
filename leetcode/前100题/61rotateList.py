"""
61 旋转链表

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        数一下链表长度lens，k=k%len，连成环，走n-k，断开，取下一个节点为返回值
        """
        if not head:
            return head
        cur = head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next
        k = k % count
        steps = count - k
        cur.next = head
        # head算1步
        while steps > 1:
            head = head.next
            steps -= 1
        newHead = head.next
        head.next = None
        return newHead


class Solution1(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        利用栈
        """
        if not head:
            return head
        stack = []
        cur = head
        nums = 0
        while cur:
            stack.append(cur)
            cur = cur.next
            nums += 1
        k = k % nums
        stack[-1].next = stack[0]
        stack[-(k + 1)].next = None
        return stack[-k]

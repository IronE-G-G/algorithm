"""
思路1：维护一个n+1长的队列，按顺序压入结点，遍历完第一个结点就是倒数n+1个结点。
思路2：双指针;让快指针先走n+1步，这样遍历完慢指针就能指在倒是n+1个结点（如果n不等于链表长度的话）
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        queue = []
        if not head:
            return None
        while head:
            queue.append(head)
            head = head.next

        if n == len(queue):
            # 写queue[1]有可能出界
            return queue[0].next

        # -(n+1)可能出界，所以需要判断n的值
        cur = queue[-(n + 1)]
        cur.next = cur.next.next
        return queue[0]


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        count = n + 1
        while count > 0 and fast:
            fast = fast.next
            count -= 1
        # n（前提有效） 为链表长度
        if count == 1:
            return head.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

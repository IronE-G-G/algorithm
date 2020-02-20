"""
86 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        创建两个链表，分别连接小于x的值和大于等于x的值，再链接起来
        """
        left = ListNode(-1)
        resLeft = left
        right = ListNode(-1)
        resRight = right
        cur = head
        while cur:
            if cur.val < x:
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next
            cur = cur.next
        left.next = resRight.next
        # 断开死循环
        right.next = None
        return resLeft.next

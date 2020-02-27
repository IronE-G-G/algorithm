"""
143 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.


1 普通递归（超时）把第一颗最后一颗摘出来，处理剩下的部分
2 存储成列表
3 快慢指针从中间分开，后边那段逆序，然后一个一个连在一起
4 递归，每次递归返回的是尾巴，因为头部跟前边的连着所以没关系
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        思路2 列表存储

        """
        if not head or not head.next or not head.next.next:
            return head
        queue = []
        while head:
            queue.append(head)
            head = head.next
        left, right = 1, len(queue) - 1
        head = queue[0]
        cur = head
        while left <= right:
            cur.next = queue[right]
            cur = cur.next
            if left == right:
                break
            cur.next = queue[left]
            cur = cur.next
            left += 1
            right -= 1
        # 不断开的话会有环
        cur.next = None
        return head


class Solution1(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        思路三 快慢指针+逆序
        """
        if not head or not head.next or not head.next.next:
            return head
        # 快慢指针找终点
        slow, fast = head, head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
        post_head = slow.next
        slow.next = None

        # 链表逆序
        def reverse(node):
            if not node or not node.next:
                return node
            post_part = reverse(node.next)
            node.next.next = node
            node.next = None
            return post_part

        reversed_post = reverse(post_head)
        pre_cur = head
        post_cur = reversed_post

        # 两个链表组合在一起
        while post_cur:
            pre_next = pre_cur.next
            post_next = post_cur.next
            pre_cur.next = post_cur
            post_cur.next = pre_next
            pre_cur = pre_next
            post_cur = post_next
        return head


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        def helper(node, lens):
            if lens == 1:
                outTail = node.next
                node.next = None
                return outTail
            if lens == 2:
                outTail = node.next.next
                node.next.next = None
                return outTail
            tail = helper(node.next, lens - 2)
            next_node = node.next
            node.next = tail
            outTail = tail.next
            tail.next = next_node
            return outTail

        helper(head, count)

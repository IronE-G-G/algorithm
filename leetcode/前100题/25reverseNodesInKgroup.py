"""
25 k个一组翻转链表 (困难)
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

思路：多指针解法+单链表翻转
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode(-1)
        pre.next = head
        res = pre
        start = head
        end = start
        count = 1
        while end:
            if count < k:
                end = end.next
                count += 1
            else:
                nextNode = end.next
                end.next = None
                pre.next = self.reverseHelper(start)
                # 翻转后start指向的那个结点变成在尾部
                start.next = nextNode

                pre = start
                start = nextNode
                end = start
                count = 1
        return res.next

    def reverseHelper(self, head):
        cur = None
        node = head
        while node:
            next_ = node.next
            node.next = cur
            cur = node
            node = next_
        return cur

    def print(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)


if __name__ == '__main__':
    listnode = ListNode(0)
    head = listnode
    for i in range(1, 6):
        listnode.next = ListNode(i)
        listnode = listnode.next
    s = Solution()
    s.print(head)
    s.print(s.reverseKGroup(head, 2))

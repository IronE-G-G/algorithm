"""
206 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        head_next = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return head_next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代
        :param head:
        :return:
        """
        if not head:
            return head
        res = None
        cur = head
        while cur:
            cur_next = cur.next
            cur.next = res
            res = cur
            cur = cur_next
        return res


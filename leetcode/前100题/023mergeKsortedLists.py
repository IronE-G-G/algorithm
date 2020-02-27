"""
23 合并k个排序链表（困难）

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
    """
    暴力解法
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        nodes = []
        for l in lists:
            while l:
                nodes.append(l)
                l = l.next
        nodes.sort(key=lambda x: x.val)
        if not nodes:
            return None
        head = nodes[0]
        cur = head
        for node in nodes[1:]:
            cur.next = node
            cur = cur.next
        return head


class Solution(object):
    """
    同时比较k个链表
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        head = ListNode(None)
        cur = head
        # 删除可能存在的空链表
        for ind in range(len(lists) - 1, -1, -1):
            if not lists[ind]:
                lists.pop(ind)
        if not lists:
            return None

        while lists:
            candidate = lists[0]
            index = 0
            # 选出下一个结点
            for ind, node in enumerate(lists):
                if node.val < candidate.val:
                    candidate = node
                    index = ind
            cur.next = candidate
            cur = cur.next
            lists[index] = lists[index].next
            # 清除变为空的链表
            if not lists[index]:
                lists.pop(index)

        return head.next

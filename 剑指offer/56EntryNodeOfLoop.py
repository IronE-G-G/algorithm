"""
链表中环的入口点：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路1：用一个set收集遍历的结点，每次遍历新结点的时候找一下结点是不是在set里面，是的话就是环的入口
思路2：快慢指针找到一个在环中的点；遍历环记录环的结点数；快指针先走一环，然后慢指针一起走。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead and not pHead.next:
            return None
        nodeSet = set()
        while pHead:
            if pHead not in nodeSet:
                nodeSet.add(pHead)
                pHead = pHead.next
            else:
                return pHead
        return None


class Solution2:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return
        slow = pHead
        fast = pHead.next
        flag = 0
        while fast and fast.next:
            if slow is fast:
                flag = 1
                break
            else:
                slow = slow.next
                fast = fast.next.next
        if flag == 0:
            return None
        else:
            cnt = 1
            slow = slow.next
            while slow is not fast:
                slow = slow.next
                cnt += 1
            slow = pHead
            fast = pHead
            for i in range(cnt):
                fast = fast.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        1.先算出长度差，然后长的先走掉那个差度，然后一起走，第一个相同的就是
        """
        len1, len2 = 0, 0
        cur1, cur2 = headA, headB
        while cur1:
            len1 += 1
            cur1 = cur1.next
        cur2 = headB
        while cur2:
            len2 += 1
            cur2 = cur2.next
        cur1, cur2 = headA, headB
        if len1 > len2:
            steps = len1 - len2
            while steps > 0:
                cur1 = cur1.next
                steps -= 1
        else:
            steps = len2 - len1
            while steps > 0:
                cur2 = cur2.next
                steps -= 1

        while cur1:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next

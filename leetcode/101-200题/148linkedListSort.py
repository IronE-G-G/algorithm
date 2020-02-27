"""
148 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        归并算法(merge sort)
        """
        if not head or not head.next:
            return head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        def mergeSort(head, lens):
            if lens == 1:
                return head
            mid = head
            count = 1
            while count < lens // 2:
                count += 1
                mid = mid.next
            right = mid.next
            mid.next = None
            # 分成两部分
            left = mergeSort(head, count)
            right = mergeSort(right, lens - count)
            res = ListNode(-1)
            cur = res
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            if right:
                cur.next = right
            else:
                cur.next = left
            return res.next

        res = mergeSort(head, count)
        return res

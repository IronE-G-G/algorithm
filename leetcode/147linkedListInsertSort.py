"""
147 对链表进行插入排序
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
示例 1：

输入: 4->2->1->3
输出: 1->2->3->4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insertion-sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = ListNode(float('-inf'))
        cur = head
        pre = res
        while cur:
            next_cur = cur.next
            guard = res
            while guard.next:
                if cur.val > guard.next.val:
                    guard = guard.next
                else:
                    break
            next_guard = guard.next
            guard.next = cur
            cur.next = next_guard
            cur = next_cur
        return res.next

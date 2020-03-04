"""
234 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    res = True

    def isPalindrome(self, head: ListNode) -> bool:
        """
        1 栈方法
        2 从中间断开迭代翻转左边的链表，对比
        """
        if not head or not head.next:
            return True
        slow, fast = head, head.next
        mid = slow.next
        while fast and fast.next:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
                mid = slow.next
            else:
                # 奇数个的话跳掉最中间的那个
                mid = slow.next.next
        # 断开
        slow.next = None

        res = None
        cur = head
        # 翻转slow部分
        while cur:
            cur_next = cur.next
            cur.next = res
            res = cur
            cur = cur_next

        while res and mid:
            if res.val != mid.val:
                return False
            res = res.next
            mid = mid.next
        return True

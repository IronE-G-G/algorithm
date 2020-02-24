"""
142 环形链表ii
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        哈希表
        floyd
        先判断有没有环，有的话根据相遇节点和步数确认环大小，fast比slow快了k个环
        再一次双指针，前面的指针比后面的快N步
        那么当慢的指针在环节点的时候就是走了前面的单向链K
        快了几个环的快指针也是单向链表长度K（因为他们速度一样）+快走的部分（N步）
        因此，快慢指针会在环节点相遇
        """
        if not head or not head.next:
            return None
        slow, fast = head, head.next
        count = 1
        while True:
            if not (slow and fast):
                return None
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            count += 1
            if slow == fast:
                break
        # # double pointers with speed=1
        slow, fast = head, head

        while count > 0:
            fast = fast.next
            count -= 1
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

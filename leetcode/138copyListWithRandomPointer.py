"""
138 复制带随机指针的链表
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        # 复制节点
        cur = head
        while cur:
            next_node = cur.next
            clone_node = Node(cur.val)
            cur.next = clone_node
            clone_node.next = next_node
            cur = next_node
        # 添加random指针
        cur = head
        while cur:
            clone_cur = cur.next
            if cur.random:
                clone_cur.random = cur.random.next
            cur = clone_cur.next
        # 拆开链表
        cur = head
        res = cur.next

        while cur:
            clone_cur = cur.next
            cur.next = clone_cur.next
            cur = cur.next
            if cur:
                clone_cur.next = cur.next
                clone_cur = clone_cur.next
        return res

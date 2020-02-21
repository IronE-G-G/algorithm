"""
109 有序链表转换二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

思路：快慢指针寻找中间节点；链表转化成数组
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        快慢指针寻找根节点；
        """

        def buildTree(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            # fast slow to find mid
            res = ListNode(-1)
            res.next = head
            preSlow = res
            slow = head
            fast = head.next
            while fast:
                fast = fast.next
                preSlow = slow
                slow = slow.next
                if fast:
                    fast = fast.next
            root = TreeNode(slow.val)
            preSlow.next = None
            leftTree = buildTree(res.next)
            rightTree = buildTree(slow.next)
            root.left = leftTree
            root.right = rightTree
            return root

        return buildTree(head)

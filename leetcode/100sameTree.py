"""
100 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        递归
        """
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left) or not self.isSameTree(p.right, q.right):
            return False
        return True


class Solution1(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        栈方法
        """

        def check(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (node1 and not node2):
                return False
            if node1.val != node2.val:
                return False
            return True

        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not check(node1, node2):
                return False
            if node1:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        return True


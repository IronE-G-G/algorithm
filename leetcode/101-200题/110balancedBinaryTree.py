"""
110 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def maxDepth(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            leftDepth = maxDepth(root.left)
            if leftDepth == -1:
                return -1
            rightDepth = maxDepth(root.right)
            if rightDepth == -1:
                return -1
            if abs(leftDepth - rightDepth) > 1:
                return -1
            return 1 + max(leftDepth, rightDepth)

        return maxDepth(root) != -1

"""
94 二叉树的中序遍历

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        中序：左中右
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        栈方法收集待处理的父节点
        """
        if not root:
            return []
        stack = [root]
        res = []

        while root.left:
            stack.append(root.left)
            root = root.left
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                nodeR = node.right
                while nodeR.left:
                    stack.append(nodeR.left)
                    nodeR = nodeR.left
        return res


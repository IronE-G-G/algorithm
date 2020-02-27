"""
107 二叉树的层次遍历ii（简单）

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        迭代
        """
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            nextQueue = []
            levels = []
            for i in range(len(queue)):
                node = queue[i]
                levels.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            res.append(levels)
            queue = nextQueue
        res.reverse()
        return res


class Solution1(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        递归的层次遍历
        """
        if not root:
            return []
        res = []

        def helper(node, level):
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        res.reverse()
        return res

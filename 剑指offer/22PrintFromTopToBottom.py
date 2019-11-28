# -*- coding:utf-8 -*-
"""
从上到下打印二叉树：从上往下打印出二叉树的每个节点，同层节点从左至右打印。
思路：层次遍历，创建一个队列，按照先进先出的规则打印结点并添加其非空子节点到队列中，直到队列为空
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

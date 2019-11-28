"""
二叉树的镜像：操作给定的二叉树，将其变换为源二叉树的镜像。
思路：递归，左右子树交换位置，再对左右子树应用镜像函数
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)

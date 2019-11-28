# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
二叉树的深度

"""
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        # 层次遍历
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1


"""
树的子结构：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
思路：函数IsSubTree判断pRoot2是不是pRoot1根节点一样的子树。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.IsSubTree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                         pRoot2)

    def IsSubTree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot2.val == pRoot1.val:
            return self.IsSubTree(pRoot1.left, pRoot2.left) and self.IsSubTree(pRoot1.right, pRoot2.right)
        else:
            return False
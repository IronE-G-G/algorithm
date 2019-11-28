# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
二叉搜索树的第k个结点
思路：求中序遍历的第k的结点
"""


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        ll = self.midSearch(pRoot)
        if 0 < k <= len(ll):
            return ll[k - 1]
        return None

    def midSearch(self, pRoot):
        if not pRoot:
            return []
        return self.midSearch(pRoot.left) + [pRoot] + self.midSearch(pRoot.right)

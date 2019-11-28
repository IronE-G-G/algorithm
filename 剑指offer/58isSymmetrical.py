# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
对称的二叉树：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
思路1：递归判断left.right right.left是否对称；left.left right.right是否对称
思路2：用队列存储每一层的结点, 判断每一层是不是对称的。
"""


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isMirror(pRoot.left, pRoot.right)

    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)


class Solution2:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot or (not pRoot.left and not pRoot.right):
            return True
        if not pRoot.left or not pRoot.right:
            return False
        level = [pRoot.left, pRoot.right]
        newLevel = []
        resLevel = []
        while level:
            for node in level:
                if not node:
                    resLevel.append('#')
                else:
                    resLevel.append(node.val)
                    newLevel.append(node.left)
                    newLevel.append(node.right)
            if resLevel == resLevel[::-1]:
                level = newLevel
                resLevel = []
                newLevel = []
            else:
                return False
        return True

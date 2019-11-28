# -*- coding:utf-8 -*-
"""
按之字形顺序打印二叉树
思路：存储每一个层的信息+reverse
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return None
        if not pRoot.left and not pRoot.right:
            return [pRoot.val]
        res = []
        level = [pRoot]
        opposite = False
        while level:
            newLevel = []
            resLevel = []
            for node in level:
                resLevel.append(node.val)
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            if opposite:
                resLevel.reverse()
                opposite = False
            else:
                opposite = True
            res.append(resLevel)
            level = newLevel
        return res


if __name__ == '__main__':
    s = Solution()
    pRoot = TreeNode(3)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(4)
    print(s.Print(pRoot))

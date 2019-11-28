"""
二叉搜索树与双向链表：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
                  要求不能创建任何新的结点，只能调整树中结点指针的指向。

思路1：中序遍历存储每个结点。再改变每个结点的指针。

思路2：递归思想，先排好左子树，全局变量pre记录已拍好的链表的最右端。
父结点的left指向pre，如果pre不为None，则pre的right指向父结点。移动pre指向父结点。
排好右子树
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution1:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        midSearchRes = self.midSearch(pRootOfTree)
        midSearchRes[0].right = midSearchRes[1]
        for ind in range(1, len(midSearchRes) - 1):
            midSearchRes[ind].left = midSearchRes[ind - 1]
            midSearchRes[ind].right = midSearchRes[ind + 1]
        midSearchRes[-1].left = midSearchRes[-2]
        return midSearchRes[0]

    def midSearch(self, pRoot):
        if not pRoot:
            return []
        return self.midSearch(pRoot.left) + [pRoot] + self.midSearch(pRoot.right)


class Solution2:
    pre = None

    def Convert(self, pRoot):
        if not pRoot:
            return pRoot
        self.ConvertHelper(pRoot)
        while self.pre.left:
            self.pre = self.pre.left
        return self.pre

    def ConvertHelper(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.ConvertHelper(pRootOfTree.left)
        pRootOfTree.left = self.pre
        if self.pre:
            self.pre.right = pRootOfTree
        self.pre = pRootOfTree
        self.ConvertHelper(pRootOfTree.right)

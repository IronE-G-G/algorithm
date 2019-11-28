# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
"""
二叉树的下一个结点：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路：根据中序遍历的性质
"""
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        # 存在右结点
        if pNode.right:
            target = pNode.right
            # 返回右结点的最左子节点
            while target and target.left:
                target = target.left
            return target
        else:
            # 存在父结点
            if pNode.next:
                # 是父节点的左结点
                if pNode.next.left is pNode:
                    return pNode.next
                # 是父节点的右结点，判断有没有爷爷结点（父节点的父节点），并且父节点是不是爷爷结点的左结点
                elif pNode.next.next and pNode.next.next.left is pNode.next:
                    return pNode.next.next
        return None
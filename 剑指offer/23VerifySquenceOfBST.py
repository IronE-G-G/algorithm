"""
二叉搜索树的后续遍历序列：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：根据后序遍历的概念（左子树-右子树-父结点）知道最后一个元素是父节点。
因为是二叉搜索数，左子树的所有结点<父结点<左子树的所有结点。
根据父结点（root）将剩余数组分成左右子树，检查右子树是不是都比root大。
是的话继续检查左右子树是不是后序遍历子树

注意：空树被判为否，但子树为空是允许的。所以要对子树做进一步的处理。
"""


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) <= 2:
            return True
        root = sequence.pop()
        split = 0
        for i in range(len(sequence)):
            if sequence[i] < root:
                split += 1
            else:
                break
        for j in range(split, len(sequence)):
            if sequence[j] < root:
                return False
        if split == 0 or len(sequence):
            return self.VerifySquenceOfBST(sequence)
        return self.VerifySquenceOfBST(sequence[:split]) and self.VerifySquenceOfBST(sequence[split:])

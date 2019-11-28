"""
重建二叉树，给树的前序遍历和中序遍历，要求重建二叉树并返回根节点
思路：前序遍历是 父结点-左子树-右子树的顺序；中序遍历是左子树-父结点-右子树的顺序。
根据前序遍历的第一个结点去找中序的该结点位置，将左右子树分开。
递归重建左右子树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        root = TreeNode(pre[0])
        rootIndInTin = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:(rootIndInTin + 1)], tin[:rootIndInTin])
        root.right = self.reConstructBinaryTree(pre[(rootIndInTin + 1):], tin[(rootIndInTin + 1):])
        return root

    def preScan(self, root):
        if not root:
            return []
        return [root.val] + self.preScan(root.left) + self.preScan(root.right)

    def tinScan(self, root):
        if not root:
            return []
        return self.tinScan(root.left) + [root.val] + self.tinScan(root.right)


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    solution = Solution()
    root = solution.reConstructBinaryTree(pre, tin)
    print(solution.preScan(root))
    print(solution.tinScan(root))

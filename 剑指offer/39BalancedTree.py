"""
平衡二叉树
解法1：遍历每个结点，获得左右子树的深度，判断该结点是否平衡
解法2：一遍计算子树深度一遍判断子树是不是平衡二叉树
"""


class Solution1:
    def getDepth(self, root):
        if not root:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def IsBalanced_Solution(self, root):
        # write code here
        if not root:
            return True
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if abs(leftDepth - rightDepth) <= 1:
            return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)
        return False


class Solution2:
    def getDepth(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth != -1 and rightDepth != -1 and abs(leftDepth - rightDepth) <= 1:
            return max(leftDepth, rightDepth) + 1
        return -1

    def IsBalanced_Solution(self, root):
        # write code here
        if not root:
            return True
        return self.getDepth(root) != -1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        递归
        """
        if not root:
            return True

        def mirror(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if (not leftNode and rightNode) or (leftNode and not rightNode):
                return False
            if leftNode.val != rightNode.val:
                return False
            if not mirror(leftNode.left, rightNode.right):
                return False
            if not mirror(leftNode.right, rightNode.left):
                return False
            return True

        return mirror(root.left, root.right)


class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        队列，将要对比的两个连续放在一起
        """
        if not root or (not root.left and not root.right):
            return True

        queue = [root.left, root.right]
        while queue:
            leftNode = queue.pop(0)
            rightNode = queue.pop(0)
            if not leftNode and not rightNode:
                continue
            if (not leftNode and rightNode) or (leftNode and not rightNode):
                return False
            if leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        return True

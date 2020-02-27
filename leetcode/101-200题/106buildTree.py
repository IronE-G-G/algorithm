"""
106 从中序和后序遍历序列构建二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    post_idx = None

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        中序：左中右
        后序：左右中

        """

        def helper(in_left, in_right):
            if in_left == in_right:
                return None
            root_val = postorder[self.post_idx]

            root = TreeNode(root_val)
            self.post_idx -= 1
            if in_left + 1 == in_right:
                return root
            rootInOrder = inorder.index(root_val)

            rightTree = helper(rootInOrder + 1, in_right)
            leftTree = helper(in_left, rootInOrder)

            root.right = rightTree
            root.left = leftTree
            return root

        self.post_idx = len(inorder) - 1
        return helper(0, len(inorder))

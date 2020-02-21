"""
105 从前序和中序遍历序列构建二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        利用root在中序的位置分割左右子树
        递归1
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        irootInOrder = inorder.index(preorder[0])
        leftInOrder = inorder[:irootInOrder]
        rightInOrder = inorder[(irootInOrder + 1):]
        leftPreOrder = preorder[1:(1 + irootInOrder)]
        rightPreOrder = preorder[(irootInOrder + 1):]
        leftTree = self.buildTree(leftPreOrder, leftInOrder)
        rightTree = self.buildTree(rightPreOrder, rightInOrder)
        root.left = leftTree
        root.right = rightTree
        return root


class Solution1(object):
    pre_idx = 0

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        递归2
        """

        def helper(in_left, in_right):
            if in_left == in_right:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            if in_left + 1 == in_right:
                return root

            loc = inorder.index(root_val)
            leftTree = helper(in_left, loc)
            rightTree = helper(loc + 1, in_right)
            root.left = leftTree
            root.right = rightTree
            return root

        return helper(0, len(preorder))

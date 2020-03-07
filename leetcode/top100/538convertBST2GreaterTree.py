"""
538 把二叉搜索树转换成累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

 

例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        右中左遍历,逆中序遍历
        """

        def rev_inOrder_traversal(root):
            stack = []
            pre_sum = 0
            node = root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.right
                node = stack.pop()
                node.val += pre_sum
                pre_sum = node.val
                node = node.left

        rev_inOrder_traversal(root)
        return root


class Solution1:
    sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        self.convertBST(root.right)
        root.val += self.sum
        self.sum = root.val
        self.convertBST(root.left)
        return root

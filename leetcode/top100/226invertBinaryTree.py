"""
226 翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        递归
        :param root:
        :return:
        """
        if not root or (not root.left and not root.right):
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        迭代，先翻父节点，再翻子节点
        """
        if not root:
            return root
        queue = [root]
        while queue:
            next_queue = []
            for node in queue:
                node.left, node.right = node.right, node.left
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return root

"""
129 求根到叶子结点数字之和
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        BFS
        """
        if not root:
            return 0
        res = 0
        queue = [(root, root.val)]
        while queue:
            next_queue = []
            for item in queue:
                node, val = item
                if not node.left and not node.right:
                    res += val
                    continue
                if node.left:
                    next_queue.append((node.left, val * 10 + node.left.val))
                if node.right:
                    next_queue.append((node.right, val * 10 + node.right.val))
            queue = next_queue

        return res


class Solution1(object):
    res = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        DFS
        """
        if not root:
            return 0

        def dfs(node, val):
            if not node.left and not node.right:
                self.res += val
                return

            if node.left:
                dfs(node.left, val * 10 + node.left.val)
            if node.right:
                dfs(node.right, val * 10 + node.right.val)

        dfs(root, root.val)
        return self.res

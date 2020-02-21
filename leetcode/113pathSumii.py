"""
31 路径总和ii
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        递归
        """
        res = []

        def helper(node, path, rest):
            if not node.left and not node.right:
                if node.val == rest:
                    res.append(path + [node.val])
                return
            rest -= node.val
            if node.left:
                helper(node.left, path + [node.val], rest)
            if node.right:
                helper(node.right, path + [node.val], rest)

        if not root:
            return res
        helper(root, [], sum)
        return res


class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        栈方法前序遍历
        """
        if not root:
            return []
        res = []

        stack = [(root, sum, [])]
        while stack:
            root, rest, path = stack.pop()
            rest -= root.val
            if not root.left and not root.right:
                if rest == 0:
                    res.append(path + [root.val])
                continue
            if root.right:
                stack.append((root.right, rest, path + [root.val]))
            if root.left:
                stack.append((root.left, rest, path + [root.val]))
        return res

"""
95 不同的二叉搜索树ii
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        递归，每个整数都作为root，小于的做左树，大于的做右子树
        """
        if n == 0:
            return []
        nums = [i for i in range(1, n + 1)]
        return self.generator(nums)

    def generator(self, candidates):
        if not candidates:
            return [None]
        if candidates == 1:
            return [TreeNode(candidates[0])]
        res = []
        for i in range(len(candidates)):
            left = self.generator(candidates[:i])
            right = self.generator(candidates[(i + 1):])
            for leftItem in left:
                for rightItem in right:
                    # root 是指针，因此要每次都生成一个
                    root = TreeNode(candidates[i])
                    root.left = leftItem
                    root.right = rightItem
                    res.append(root)
        return res

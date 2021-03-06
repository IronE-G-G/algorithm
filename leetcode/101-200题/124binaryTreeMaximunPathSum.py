"""
124 二叉树的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    maximun = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxGain(node):
            if not node:
                return 0

            left_gain = max(0, maxGain(node.left))
            right_gain = max(0, maxGain(node.right))
            # 以node为最顶点且串联左右的两条路径
            self.maximun = max(self.maximun, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        maxGain(root)
        return self.maximun

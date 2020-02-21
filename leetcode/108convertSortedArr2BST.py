"""
108 将有序数组转化成二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        答案不是唯一的原因是当数组长度为偶数的时候
        构建的树的根节点既能选中间偏左也能选中间偏右的元素

        """

        def helper(left, right):
            if left == right:
                return None
            # 保证所有左右子树的元素数量相差不大于1
            iroot = (left + right) // 2
            root = TreeNode(nums[iroot])
            if left + 1 == right:
                return root
            leftTree = helper(left, iroot)
            rightTree = helper(iroot + 1, right)

            root.left = leftTree
            root.right = rightTree

            return root

        return helper(0, len(nums))

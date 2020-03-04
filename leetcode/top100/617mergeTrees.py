"""
617 合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        前序遍历
        :param t1:
        :param t2:
        :return:
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


class Solution1:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        层次遍历
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val+=t2.val
        # 保证队列里面的每一组元素都不是空
        queue = [(t1,t2)]
        while queue:
            queue_next = []
            for node1, node2 in queue:
                if not node2.left and not node2.right:
                    continue
                if node2.left:
                    if node1.left:
                        node1.left.val+=node2.left.val
                        queue.append((node1.left, node2.left))
                    else:
                        node1.left = node2.left
                if node2.right:
                    if node1.right:
                        node1.right.val+=node2.right.val
                        queue.append((node1.right, node2.right))
                    else:
                        node1.right = node2.right
            queue = queue_next
        return t1

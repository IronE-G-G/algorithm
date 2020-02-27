"""
199 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        1 层次遍历返回最右的那个
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node = queue[i]
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            res.append(queue[-1].val)
            queue = next_queue
        return res


class Solution1:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        dfs
        """
        if not root:
            return []
        left_tree_right_view = self.rightSideView(root.left)
        right_tree_right_view = self.rightSideView(root.right)
        len_right = len(right_tree_right_view)
        return [root.val] + right_tree_right_view + left_tree_right_view[len_right:]

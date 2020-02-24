"""
145 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

类似题目： 94 中序遍历 102 层次遍历 144 前序遍历

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        递归
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]


class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        栈方法+哈希表
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        stack = [root]
        res = []
        visited = set()
        while stack:
            node = stack[-1]
            if (not node.left and not node.right) or (node.right and node.right in visited) or (
                    node.left and node.left in visited):
                res.append(node.val)
                stack.pop()
                visited.add(node)
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Solution2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        栈方法(出栈中右左)+逆序
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

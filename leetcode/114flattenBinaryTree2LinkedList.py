# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        栈方法前序遍历展开为链表
        """
        if not root:
            return None
        stack = [root]
        res = TreeNode(-1)
        pre = res
        while stack:
            node = stack.pop()
            pre.right = node
            pre = pre.right

            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                stack.append(node.left)
                node.left = None

        return res.right


class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        递归
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        preOrderLeft = self.flatten(root.left)
        root.left = None
        preOrderRight = self.flatten(root.right)
        root.right = None
        root.right = preOrderLeft
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = preOrderRight

        return root

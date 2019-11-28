"""
二叉树中和为某值的路径
思路：广度遍历每一条路径然后检查他们的和是否为该值。
"""


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    number = -1

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        self.number = expectNumber
        self.BFS(root, [root.val], result)
        return result

    def BFS(self, node, path, res):
        if not node.left and not node.right:
            if sum(path) == self.number:
                res.append(path)
        if node.left:
            self.BFS(node.left, path + [node.left.val], res)
        if node.right:
            self.BFS(node.right, path + [node.right.val], res)

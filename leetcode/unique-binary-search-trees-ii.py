# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print(self):
        if not self.left:
            left = []
        else:
            left = self.left.print()
        if not self.right:
            right = []
        else:
            right = self.right.print()
        res = []
        res.extend(left)
        res.append(self.val)
        res.extend(right)
        return res.__str__()


a = TreeNode(3)
a.left = TreeNode(2)

print(a)


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateSubTrees(n, 0)

    def generateSubTrees(self, n, offset):
        if n == 0:
            return [None]
        res = []
        for i in range(1, n + 1):
            left = self.generateSubTrees(i - 1, offset)
            right = self.generateSubTrees(n - i, i + offset)
            for leftSubtree in left:
                for rightSubTree in right:
                    root = TreeNode(i + offset)
                    root.left = leftSubtree
                    root.right = rightSubTree
                    res.append(root)
        return res


class Solution(object):
    """
    dp method
    """
    def generateTrees(self, n):
        trees = [[]]
        if n == 0:
            return trees[0]
        trees[0].append(None)
        for lens in range(1, n + 1):
            res = []
            for root in range(1, lens + 1):
                for leftSubTree in trees[root - 1]:
                    for rightSubTree in trees[lens - root]:
                        tree = TreeNode(root)
                        tree.right = self.clone(rightSubTree, root)
                        tree.left = leftSubTree
                        res.append(tree)

            trees.append(res)
        return trees[n]

    def clone(self, node, offset):
        if not node:
            return None
        new = TreeNode(node.val + offset)
        new.left = self.clone(node.left, offset)
        new.right = self.clone(node.right, offset)
        return new




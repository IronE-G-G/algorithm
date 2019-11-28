# -*- coding:utf-8 -*-
"""
序列化二叉树：前序遍历做法
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        nodes = s.split(',')
        return self.DeserializeHelper(nodes)

    def DeserializeHelper(self, ll):
        if not ll:
            return None
        val = ll.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.DeserializeHelper(ll)
            root.right = self.DeserializeHelper(ll)
        return root


if __name__ == '__main__':
    s = Solution()
    pRoot = TreeNode(3)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(4)
    serial = s.Serialize(pRoot)
    root = s.Deserialize(serial)
    serial1 = s.Serialize(root)
    print(serial)
    print(serial1)

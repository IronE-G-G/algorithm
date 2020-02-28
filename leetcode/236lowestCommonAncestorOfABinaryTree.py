"""
236 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        层次遍历并保存节点的父节点，找搭配p和q之后，先收集p的所有祖先节点，再遍历q的祖先节点，返回第一个在p祖先集合中的祖先节点
        """
        stack = [root]
        parents = {root: None}
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        while q:
            if q in ancestors:
                return q
            q = parents[q]


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        dfs先找直接到那两个的路径，再比较；
        所有节点遍历一遍
        路径比较 最后一个相同的祖先节点，复杂度为O(K)，K是树高度
        """
        path_p = []
        path_q = []

        def node_search(node, path):
            if not node:
                return

            path = path + [node]
            if node == p:
                path_p.extend(path)
            if node == q:
                path_q.extend(path)
            if path_p and path_q:
                return
            node_search(node.left, path)
            node_search(node.right, path)

        node_search(root, [])
        # path compare
        pre_common = 0
        cur = 1
        while cur < min(len(path_p), len(path_q)):
            if path_p[cur] != path_q[cur]:
                return path_p[pre_common]
            pre_common = cur
            cur += 1
        return path_p[pre_common]

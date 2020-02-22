"""
116 填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        层次遍历，按层加指针
        """
        if not root:
            return None
        queue = [root]
        while queue:
            nextQueue = []
            levels = []
            for i in range(len(queue)):
                node = queue[i]
                levels.append(node)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            for i in range(len(levels) - 1):
                levels[i].next = levels[i + 1]
            queue = nextQueue
        return root


class Solution1(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        空间复杂度为常数
        """
        if not root:
            return None
        head = root
        while head.left:
            leftMost = Node()
            cur = leftMost
            while head:
                cur.next = head.left
                cur = cur.next
                cur.next = head.right
                cur = cur.next
                head = head.next
            head = leftMost.next

        return root

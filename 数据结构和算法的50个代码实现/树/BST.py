
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    """
    二叉搜索树的插入，删除，搜索
    遍历：中序遍历（迭代，递归），层次遍历，前序遍历(迭代，递归)，后续遍历(迭代，递归)
    搜索：某节点的前一个节点，后一个节点
    """

    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        找到可以插入的空位，记录父亲节点和空位是父亲的左孩子还是右孩子
        :param val:
        :return:
        """
        if not self.root:
            self.root = TreeNode(val)
            return
        cur = self.root
        father = None
        setRight = True
        while cur:
            if cur.val == val:
                return -1
            father = cur

            if cur.val < val:
                cur = cur.right
                setRight = True
            else:
                cur = cur.left
                setRight = False
        if setRight is True:
            father.right = TreeNode(val)
        else:
            father.left = TreeNode(val)

    def search(self, val):
        """
        :param val:
        :return:返回节点
        """
        if not self.root:
            return -1
        cur = self.root
        while cur:
            if cur.val == val:
                return cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return -1

    def delete(self, val):
        """
        保存父亲节点，找到节点后判断
        1 节点没有孩子节点：直接删除
        2 有一个：父亲指向它的指针指向该孩子节点
        3 有两个：找到右子树的最小节点，替代该节点的值，删除那个最小节点
        4 根结点跟普通节点的delete不一样
        :param val:
        :return:
        """
        if not self.root:
            return -1

        cur = self.root
        father = None
        right = True
        while cur:
            if cur.val == val:
                break
            father = cur
            if cur.val > val:
                cur = cur.left
                right = False
            else:
                cur = cur.right
                right = True
        # 没有找到节点
        if not cur:
            return -1
        # 1
        if not cur.left and not cur.right:
            # 根节点
            if cur == self.root:
                self.root = None
                return
            # 普通节点
            if right is True:
                father.right = None
            else:
                father.left = None
            return
        # 3
        if cur.left and cur.right:
            right_child = cur.right
            # 右子树没有左节点
            if not right_child.left:
                cur.val = right_child.val
                cur.right = right_child.right
                return
            # 右节点有左子节点
            pre = None
            while right_child.left:
                pre = right_child
                right_child = right_child.left
            # 赋值给cur
            cur.val = right_child.val
            # 删除该节点
            if not right_child.right:
                pre.left = None
            else:
                pre.left = right_child.right
            return

        # 2
        child = cur.left if cur.left else cur.right
        if cur == self.root:
            self.root = child
            return
        if right is True:
            father.right = child
        else:
            father.left = child

    def bfs(self):
        """
        层次遍历
        :return:
        """
        if not self.root:
            return []
        queue = [self.root]
        res = []
        while any(queue):
            queue_next = []
            for node in queue:
                if not node:
                    res.append(-1)
                    continue
                res.append(node.val)
                queue_next.append(node.left)
                queue_next.append(node.right)
            queue = queue_next

        return res

    def prev_search(self, val):
        """
        中序遍历+前向指针
        :param val: int
        :return: TreeNode
        """
        stack = []
        cur = self.root
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val == val:
                if res:
                    return res[-1]
                return -1
            res.append(cur.val)
            cur = cur.right
        return -1

    def post_search(self, val):
        """
        1 中序遍历
        :param val:
        :return:
        """
        cur = self.root
        stack = []
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if res and res[-1] == val:
                return cur.val
            res.append(cur.val)
            cur = cur.right
        return -1


if __name__ == '__main__':
    from random import randint
    from Traversal import *
    bst = BST()
    print('insert:')
    for i in range(20):
        val = randint(1, 20)
        print(val)
        bst.insert(val)
    print('delete:')
    for i in range(3):
        val = randint(1, 7)
        print(val)
        bst.delete(val)
    print('bfs:')
    print(bst.bfs())
    print('inorder traversal:')
    print(inorder_traversal(bst.root))
    print(inorder_recursion(bst.root))
    print('next node value of 3:')
    print(bst.post_search(3))
    print(bst.prev_search(3))
    print('preorder traversal:')
    print(preorder_recursion(bst.root))
    print(preorder_traversal(bst.root))
    print('postorder traversal:')
    print(postorder_traversal(bst.root))
    print(postorder_recursion(bst.root))





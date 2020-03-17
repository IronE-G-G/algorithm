def preorder_recursion(root):
    if not root:
        return []
    return [root.val] + preorder_recursion(root.left) + preorder_recursion(root.right)


def preorder_traversal(root):
    stack = []
    cur = root
    res = []
    while stack or cur:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        cur = cur.right
    return res


def postorder_recursion(root):
    if not root:
        return []
    return postorder_recursion(root.left) + postorder_recursion(root.right) + [root.val]


def postorder_traversal(root):
    """
    中右左 然后结果逆序
    :param root:
    :return:
    """
    stack = []
    cur = root
    res = []
    while stack or cur:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.right
        cur = stack.pop()
        cur = cur.left
    return res[::-1]


def inorder_recursion(root):
    if not root:
        return []
    return inorder_recursion(root.left) + [root.val] + inorder_recursion(root.right)


def inorder_traversal(root):
    """
    左中右
    :param root:
    :return:
    """
    cur = root
    stack = []
    res = []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedStack:
    """
    栈顶是链表的头部
    """

    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return -1
        val = self.top.val
        self.top = self.top.next
        return val

    def __repr__(self):
        cur = self.top
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return '[' + ','.join(str(x) for x in res) + ']'


if __name__ == '__main__':
    stack = LinkedStack()
    stack.pop()
    stack.push(1)
    stack.pop()
    stack.push(1)
    stack.push(4)
    print(stack)

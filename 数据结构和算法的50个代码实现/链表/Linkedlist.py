class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """
    实现单链表类，增删节点
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

    def pop(self, val):
        """
        pop第一个值为val的节点
        :return: pop的值，没有返回-1
        """
        if self.head is None:
            return -1
        cur = self.head
        pre = None
        while cur:
            if cur.val != val:
                pre = cur
                cur = cur.next
            else:
                break
        if cur is None:
            return -1
        if cur == self.head:
            self.head = self.head.next
            return cur.val
        pre.next = cur.next
        return cur.val

    def print(self):
        cur = self.head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)


if __name__ == '__main__':
    l = LinkedList()
    l.append(3)
    l.append(4)
    l.append(5)
    l.print()
    l.pop(5)
    l.print()
    l.pop(3)
    l.print()


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.top = None
        self.helper = None

    def delete_from_head(self):
        if not self.top:
            if not self.helper:
                return -1
            val = self.helper.val
            self.helper = self.helper.next
            return val
        while self.top:
            next_node = self.top.next
            self.top.next = self.helper
            self.helper = self.top
            self.top = next_node
        val = self.helper.val
        next_node = self.helper.next
        self.helper.next = next_node.next
        return val

    def append_to_tail(self, val):
        while self.helper:
            next = self.helper.next
            self.helper.next = self.top
            self.top = self.helper
            self.helper = next
        node = Node(val)
        node.next = self.top
        self.top = node


if __name__ == '__main__':
    queue = LinkedQueue()
    queue.append_to_tail(2)
    queue.append_to_tail(1)
    queue.delete_from_head()
    queue.delete_from_head()
    queue.delete_from_head()

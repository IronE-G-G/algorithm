class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    O(1)的复杂度增删改查key的值，双向链表+哈希表
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashMap = dict()

    def move_to_end(self, key):
        if key not in self.hashMap:
            return
        node = self.hashMap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def pop_from_head(self):
        if self.head.next == self.tail:
            return -1
        head_next = self.head.next
        self.head.next = head_next.next
        head_next.next.prev = self.head
        self.hashMap.pop(head_next.key)
        del head_next

    def push(self, key, value):
        if key in self.hashMap:
            self.move_to_end(key)
            node = self.hashMap[key]
            node.val = value
        else:
            if self.hashMap.__len__() == self.capacity:
                self.pop_from_head()

            node = Node(key, value)
            self.hashMap[key] = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key):
        if key not in self.hashMap:
            return -1
        self.move_to_end(key)
        return self.hashMap[key].val

    def print_all(self):
        cur = self.head
        res = []
        while cur:
            res.append((cur.key, cur.val))
            cur = cur.next
        print(res[1:-1])


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.push('a', 1)
    lru.push('b', 2)
    lru.push('c', 3)
    lru.get('b')
    lru.push('d', 4)
    lru.push('c', 5)
    lru.print_all()

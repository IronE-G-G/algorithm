class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    """
    模拟链地址解决哈希冲突
    """
    def __init__(self, mod_value):
        self.address = [None for _ in range(mod_value)]
        self.mod_value = mod_value

    def add(self, key, value):
        i = key % self.mod_value
        # 开放地址
        if not self.address[i]:
            self.address[i] = Node(key, value)
            return
        cur = self.address[i]
        pre = None
        # key是否存在
        while cur:
            if cur.key == key:
                cur.value = value
                return
            pre = cur
            cur = cur.next
        pre.next = Node(key, value)
        return

    def get(self, key):
        i = key % self.mod_value
        if not self.address[i]:
            return -1
        cur = self.address[i]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def pop(self, key):
        i = key % self.mod_value
        if not self.address[i]:
            return -1
        # 头部即为所求
        if self.address[i].key == key:
            value = self.address[i].value
            self.address[i] = self.address[i].next
            return value

        pre = None
        cur = self.address[i]
        while cur:
            if cur.key == key:
                pre.next = cur.next
                return cur.value
            pre = cur
            cur = cur.next
        return -1


if __name__ == '__main__':
    hashmap = HashMap(12)
    for i in range(0, 20, 2):
        hashmap.add(i, i * 2)
    print(hashmap.get(3))
    print(hashmap.get(4))
    print(hashmap.pop(3))

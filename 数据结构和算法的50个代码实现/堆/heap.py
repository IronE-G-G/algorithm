class Heap:
    def __init__(self, arr):
        """
        小顶堆
        :param capacity:
        """
        self.heap = arr
        self.capacity = len(arr)
        self._build()

    def adjust(self, i):
        if i >= len(self.heap):
            return
        left = 2 * i + 1
        right = 2 * i + 2
        min_i = i
        if left < self.capacity and self.heap[left] < self.heap[min_i]:
            min_i = left
        if right < self.capacity and self.heap[right] < self.heap[min_i]:
            min_i = right
        if min_i != i:
            self.heap[min_i], self.heap[i] = self.heap[i], self.heap[min_i]
            self.adjust(min_i)

    def _build(self):
        for i in range(len(self.heap) // 2 + 1, -1, -1):
            self.adjust(i)

    def push(self, val):
        pre = self.heap[0]
        if val > self.heap[0]:
            self.heap[0] = val
            self.adjust(0)
            return pre
        return -1

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self.capacity -= 1
        self.adjust(0)
        return val


if __name__ == '__main__':
    heap = Heap([1, 5, 6, 4, 2, 1, 4])
    from random import randint

    for i in range(7):
        val = randint(4, 17)
        print('value:', val)
        print('poping value:')
        print(heap.push(val))
        print(heap.heap)

    res = []
    while heap.heap:
        res.append(heap.pop())
    print(res)

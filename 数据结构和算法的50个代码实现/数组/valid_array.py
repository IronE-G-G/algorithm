class Array:
    """
    实现一个大小固定的有序数组，支持动态增删改操作
    """
    def __init__(self, size):
        self._arr = []
        self._size = size

    def push(self, item):
        if self._arr.__len__() == self._size:
            return False
        i = 0
        while i < len(self._arr):
            if self._arr[i] >= item:
                break
            i += 1
        self._arr.insert(i, item)
        return True

    def modify(self, item, index):
        if index >= self._size:
            return False
        self._arr[index] = item
        return True

    def pop(self, index=-1):
        try:
            self._arr.pop(index)
            return True
        except IndexError:
            return False

    def print(self):
        print([num for num in self._arr])


if __name__ == '__main__':
    arr = Array(5)
    arr.push(3)
    arr.push(2)
    arr.pop(4)
    arr.pop()
    arr.pop()
    arr.pop()
    arr.print()
    arr.push(1)
    arr.print()

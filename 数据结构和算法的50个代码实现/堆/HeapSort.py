class Solution:
    def getLeastNumbers(self, arr, k):
        """
        大顶堆
        """
        if k <= 0:
            return []
        heap = arr[:k]

        def adjust(i, lens):
            left, right = 2 * i + 1, 2 * i + 2
            max_i = i
            if left < lens and heap[left] > heap[max_i]:
                max_i = left
            if right < lens and heap[right] > heap[max_i]:
                max_i = right
            if max_i != i:
                heap[max_i], heap[i] = heap[i], heap[max_i]
                adjust(max_i, lens)

        # 建堆
        for i in range(len(heap) - 1, -1, -1):
            adjust(i, len(heap))
        # insert
        for num in arr[k:]:
            if num < heap[0]:
                heap[0] = num
                adjust(0, len(heap))

        # 对结果排序
        last = len(heap) - 1
        while last > 0:
            heap[0], heap[last] = heap[last], heap[0]
            adjust(0, last)
            last -= 1
        return heap


if __name__ == '__main__':
    from random import randint
    arr = [randint(1, 19) for _ in range(9)]
    print(arr)
    s = Solution()

    print(s.getLeastNumbers(arr, 3))

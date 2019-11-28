# -*- coding:utf-8 -*-
"""
数组中的逆序对
思路：暴力解法（冒泡排序），归并排序
"""


# -*- coding:utf-8 -*-
class Solution1:
    cnt = 0

    def InversePairs(self, data):
        # write code here
        self.bubbleSort(data)
        return self.cnt % 1000000007

    def bubbleSort(self, arr):
        arrLen = len(arr)
        if arrLen <= 1:
            return
        while arrLen > 1:
            for i in range(0, arrLen - 1):
                if arr[i] > arr[i + 1]:
                    self.cnt += 1
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            arrLen -= 1


class Solution2:
    cnt = 0

    def InversePairs(self, data):
        # write code here
        sortedData = self.mergeSort(data)
        return self.cnt % 1000000007

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        if len(arr) == 2:
            if arr[0] > arr[1]:
                self.cnt += 1
                arr[0], arr[1] = arr[1], arr[0]
            return arr
        cur = len(arr) // 2
        left = self.mergeSort(arr[:cur])
        right = self.mergeSort(arr[cur:])
        res = []
        r, l = 0, 0
        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                res.append(right[r])
                r += 1
                self.cnt += len(left) - l
            else:
                res.append(left[l])
                l += 1
        return res + left[l:] + right[r:]

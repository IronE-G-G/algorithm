# -*- coding:utf-8 -*-
"""

"""
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        start_pos = self.firstkBiSearch(data, k)
        if start_pos == -1:
            return 0
        end_pos = self.lastkBiSearch(data, k)
        return end_pos - start_pos + 1

    def firstkBiSearch(self, arr, k):
        if not arr:
            return -1
        start, end = 0, len(arr) - 1
        while start <= end:
            cur = (start + end) // 2
            if k > arr[cur]:
                start = cur + 1
            elif k == arr[cur] and (cur == 0 or arr[cur - 1] < k):
                return cur
            else:
                end = cur - 1
        return -1

    def lastkBiSearch(self, arr, k):
        if not arr:
            return -1
        start, end = 0, len(arr) - 1
        while start <= end:
            cur = (start + end) // 2
            if k < arr[cur]:
                end = cur - 1
            elif k == arr[cur] and cur == len(arr) - 1 or arr[cur + 1] > k:
                return cur
            else:
                start = cur + 1
        return -1


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 2, 3, 4]
    print(NumOfKSearch(arr, 1))

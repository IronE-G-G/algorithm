# -*- coding:utf-8 -*-
"""
数据流中的中位数
思路：维护一个排序数组，二分查找插入位置；
注意：牛客网上的剑指offer题库中这道题的运行有bug
"""


class Solution:
    sortArr = []
    length = 0

    def Insert(self, num):
        # write code here
        if self.length == 0:
            self.sortArr.append(num)
            self.length = 1
        else:
            loc = self.binarySearch(num)
            self.sortArr.insert(loc, num)
            self.length += 1

    def GetMedian(self, arr):
        # write code here
        if self.length & 1 == 1:
            return self.sortArr[self.length >> 1]
        else:
            mid = self.length >> 1
            return (self.sortArr[mid - 1] + self.sortArr[mid]) / 2

    def binarySearch(self, num):
        start, end = 0, self.length - 1
        while start <= end:
            center = (start + end) // 2
            if self.sortArr[center] <= num:
                start = center + 1
            else:
                end = center - 1
        return start


if __name__ == '__main__':
    arr = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    s = Solution()
    res = []
    for item in arr:
        s.Insert(item)
        print(s.sortArr)
        print(s.length)
        res.append(s.GetMedian(arr))
    print(res)

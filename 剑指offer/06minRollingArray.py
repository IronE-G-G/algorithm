# -*- coding:utf-8 -*-
"""
旋转数组的最小数字，非递减排序数组的旋转
思路：二分查找的衍生，注意终止条件。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # binary search
        if not rotateArray:
            return 0
        start, end = 0, len(rotateArray) - 1
        ind = (start + end) // 2
        while (end - start) > 1:
            if rotateArray[ind] > rotateArray[end]:
                start = ind
            else:
                end = ind
            ind = (start + end) // 2
        return min(rotateArray[start], rotateArray[end])
        # write code here


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 3, 0, 0, 0, 1]
    s = Solution()
    print(s.minNumberInRotateArray(arr))

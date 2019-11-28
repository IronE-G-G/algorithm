# -*- coding:utf-8 -*-
"""
数组中出现次数超过一半的数字
思路：使用字典保存出现的次数。之后对次数进行判断
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numCount = dict()
        for num in numbers:
            if num not in numCount:
                numCount[num] = 1
            else:
                numCount[num] = numCount[num] + 1
        threshold = len(numbers) / 2
        for key, value in numCount.items():
            if value > threshold:
                return key
        return 0


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(arr))

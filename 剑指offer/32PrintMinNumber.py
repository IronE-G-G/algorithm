# -*- coding:utf-8 -*-
"""
把数组排成最小的数
思路：设计比较规则，如果字符串ab>ba，那么a>b，a，b需要交换
"""


def str_sort(s1, s2):
    if s1 + s2 < s2 + s1:
        return -1
    elif s1 + s2 == s2 + s1:
        return 0
    else:
        return 1


class Solution:
    def PrintMinNumber(self, numbers):
        sorted_arr = self.fastSort(list(map(str, numbers)))
        return ''.join(sorted_arr)
        # write code here

    def fastSort(self, numbers):
        if len(numbers) <= 1:
            return numbers
        cur = len(numbers) // 2
        left = []
        right = []
        mid = []
        for item in numbers:
            compare = str_sort(item, numbers[cur])
            if compare == -1:
                left.append(item)
            elif compare == 0:
                mid.append(item)
            else:
                right.append(item)
        left = self.fastSort(left)
        right = self.fastSort(right)
        return left + mid + right


if __name__ == '__main__':
    arr = [3, 4, 1, 2, 4]
    s = Solution()
    print(s.PrintMinNumber(arr))

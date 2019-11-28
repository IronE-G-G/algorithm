# -*- coding:utf-8 -*-
"""
调整数组顺序使得奇数在偶数前面：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
思路1：使用两个列表一个存奇数一个偶数，遍历数组将奇数和偶数分开。时间和空间复杂度为O(n)
思路2：类似冒泡排序的做法，遍历找到一个奇数，然后从他开始从后往前找有没有偶数。
"""


class Solution1:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return []
        odd = []
        even = []
        for i in array:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)
        return odd + even


class Solution2:
    def reOrderArray(self, array):
        if not array:
            return []
        for i in range(1, len(array)):
            # array[i]是否是奇数
            if array[i] & 1 == 1:
                j = i - 1
                ind = i
                while j >= 0:
                    if array[j] & 1 == 0:
                        array[j], array[ind] = array[ind], array[j]
                        # 记录原先那个奇数的位置
                        ind = j
                        j = ind - 1
                    else:
                        j -= 1
        return array
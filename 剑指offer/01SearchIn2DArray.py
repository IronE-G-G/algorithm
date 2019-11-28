# -*- coding:utf-8 -*-
"""
二维数组中的查找：数组从左到右，从上到下递增，判断一个整数在数组中是否存在
思路：从左下角或右上角开始，不断跟target判断，比如从左下角开始，如果位置所在的数比target大，则向上走，小则向右走。
注意：判断是否出界
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        nrow, ncol = len(array), len(array[0])
        rowId = nrow - 1
        colId = 0
        while rowId >= 0 and colId < ncol:
            if array[rowId][colId] == target:
                return True
            elif array[rowId][colId] > target:
                rowId -= 1
            else:
                colId += 1
        return False

"""
顺时针打印矩阵：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
思路：设置4个指针分别管理左上右下还没打印的行列，每次顺序打印四条边框，指针向内移动，并判断指针是否过界(up>down,left>right)。
如果存在指针过界则证明没有可以打印的数了。
"""


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        left, up, right, down = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        res = []
        while True:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down:
                break
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if right < left:
                break
        return res

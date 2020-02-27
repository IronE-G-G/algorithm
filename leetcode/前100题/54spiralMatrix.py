"""
54 螺旋矩阵（中等）
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

思路：4个指针约束打印范围
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left, top, right, down = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        res = []
        while True:
            if top <= down:
                for j in range(left, right + 1):
                    res.append(matrix[top][j])
                top += 1
            if top > down:
                break
            if right >= left:
                for i in range(top, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if right < left:
                break

            if down >= top:
                for j in range(right, left - 1, -1):
                    res.append(matrix[down][j])
                down -= 1

            if left <= right:
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res

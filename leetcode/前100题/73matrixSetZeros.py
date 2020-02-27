"""
73 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        空间复杂度O(m+n)
        """
        row0 = set()
        col0 = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row0.add(i)
                    col0.add(j)
        for i in range(m):
            for j in range(n):
                if i in row0 or j in col0:
                    matrix[i][j] = 0


class Solution1(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        使用两个指针标志第一行和第一列是否要为0
        再用第一行和第一列分别作为其他列和行置为0的标志，
        空间复杂度为O(1)
        """
        nrow, ncol = len(matrix), len(matrix[0])
        firstRow = False
        firstCol = False
        for col in range(ncol):
            if matrix[0][col] == 0:
                firstRow = True
                break
        for row in range(nrow):
            if matrix[row][0] == 0:
                firstCol = True
                break
        for i in range(1, nrow):
            for j in range(1, ncol):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, nrow):
            for j in range(1, ncol):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstRow:
            matrix[0] = [0 for _ in range(ncol)]
        if firstCol:
            for row in range(nrow):
                matrix[row][0] = 0
        return matrix

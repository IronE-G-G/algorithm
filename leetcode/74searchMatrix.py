"""
74 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        二分法，空间复杂度O(log(mn))
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            irow = mid // n
            icol = mid % n
            if matrix[irow][icaol] == target:
                return True
            elif matrix[irow][icol] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        O(max(m,n))
        """
        if not matrix:
            return False
        nrow, ncol = len(matrix), len(matrix[0])
        irow, icol = nrow - 1, 0
        while 0 <= irow < nrow and 0 <= icol < ncol:
            if matrix[irow][icol] == target:
                return True
            elif matrix[irow][icol] > target:
                irow -= 1
            else:
                icol += 1
        return False

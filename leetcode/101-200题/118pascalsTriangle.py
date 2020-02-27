"""
118 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            origin = [1]
            for j in range(len(res[-1]) - 1):
                origin.append(res[-1][j] + res[-1][j + 1])
            origin.append(1)
            res.append(origin)
        return res

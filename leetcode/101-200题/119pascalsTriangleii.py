"""
119 杨辉三角ii
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        迭代/dp
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        preRow = [1, 1]
        for i in range(2, rowIndex + 1):
            current_row = [1]
            for j in range(len(preRow) - 1):
                current_row.append(preRow[j] + preRow[j + 1])
            current_row.append(1)
            preRow = current_row
        return preRow

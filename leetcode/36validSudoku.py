"""
36 有效的数独（中等）
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

数独部分空格内已填入了数字，空白格用 '.' 表示。

"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row check
        for i in range(9):
            if not self.duplicateCheck(board[i]):
                return False
        # col check
        for icol in range(9):
            col = [x[icol] for x in board]
            if not self.duplicateCheck(col):
                return False
        # block check
        for irow in range(0, 9, 3):
            for jcol in range(0, 9, 3):
                block = [board[i][j] for i in range(irow, irow + 3) for j in range(jcol, jcol + 3)]
                if not self.duplicateCheck(block):
                    return False

        return True

    def duplicateCheck(self, nums):
        res = set()
        for char in nums:
            if char != '.':
                if char not in res:
                    res.add(char)
                else:
                    return False
        return True


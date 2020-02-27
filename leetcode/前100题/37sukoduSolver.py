"""
37 解数独 （困难）
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

思路：约束，回溯
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rowValues = [set([str(x) for x in range(1, 10)]) for i in range(9)]
        colValues = [set([str(x) for x in range(1, 10)]) for i in range(9)]
        blockValues = [set([str(x) for x in range(1, 10)]) for i in range(9)]
        candidate = []
        # initialize
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rowValues[i].remove(board[i][j])
                    colValues[j].remove(board[i][j])
                    blockValues[(i // 3) * 3 + j // 3].remove(board[i][j])
                else:
                    candidate.append((i, j))

        def backtarck(index=0):
            if index == len(candidate):
                return True
            i, j = candidate[index]
            iblock = (i // 3) * 3 + j // 3
            for value in rowValues[i] & colValues[j] & blockValues[iblock]:
                rowValues[i].remove(value)
                colValues[j].remove(value)
                blockValues[iblock].remove(value)
                board[i][j] = value
                if backtarck(index + 1):
                    return True
                rowValues[i].add(value)
                colValues[j].add(value)
                blockValues[iblock].add(value)
            return False

        backtarck()
        return board

"""
79 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

类似题目：130 包围区域；200 岛屿数量
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        dfs
        """

        def dfs(board, word, i, j):
            if not word:
                return True
            # 越界或不相等
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            # else
            value = board[i][j]
            board[i][j] = '0'
            res = dfs(board, word[1:], i + 1, j) or dfs(board, word[1:], i - 1, j) or dfs(board, word[1:], i,
                                                                                          j - 1) or dfs(board, word[1:],
                                                                                                        i, j + 1)
            board[i][j] = value
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j):
                    return True
        return False

"""
52 N皇后ii（困难）

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
问多少种解法
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        回溯算法
        """
        res = []

        def backtrack(path, n):
            if len(path) == n:
                res.append(path)
                return
            jrow = len(path)
            for jcol in range(n):
                if jcol not in path:
                    flag = True
                    for irow, icol in enumerate(path):
                        if abs(irow - jrow) == abs(icol - jcol):
                            flag = False
                            break
                    if flag:
                        backtrack(path + [jcol], n)

        backtrack([], n)

        return len(res)

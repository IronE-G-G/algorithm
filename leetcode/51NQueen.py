"""
51 N皇后（困难）

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
"""


class Solution(object):
    def solveNQueens(self, n):
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
        queenImage = [['.' * i + 'Q' + '.' * (n - i - 1) for i in item] for item in res]

        return queenImage


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))

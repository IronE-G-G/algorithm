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

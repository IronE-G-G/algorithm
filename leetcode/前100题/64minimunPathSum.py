"""
64 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。


"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        dp
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                elif i == m - 1:
                    dp[i][j] = dp[i][j + 1] + grid[i][j]
                elif j == n - 1:
                    dp[i][j] = dp[i + 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return dp[0][0]

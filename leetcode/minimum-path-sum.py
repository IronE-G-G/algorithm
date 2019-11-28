class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        minSum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    minSum[i][j] = grid[i][j]
                elif i == m-1:
                    minSum[i][j] = grid[i][j]+minSum[i][j+1]
                elif j == n-1:
                    minSum[i][j] = grid[i][j] + minSum[i+1][j]
                else:
                    minSum[i][j] = grid[i][j] + min(minSum[i][j+1], minSum[i+1][j])

        return minSum[0][0]



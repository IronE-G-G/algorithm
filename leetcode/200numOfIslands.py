"""
200 岛屿数量
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        dfs
        对每个元素都dfs
        count在外面
        dfs负责把传进去的区域变为0
        """
        if not grid:
            return 0
        nrow, ncol = len(grid), len(grid[0])
        matrix = [[char for char in grid[i]] for i in range(nrow)]
        count = 0

        def dfs(i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or matrix[i][j] == '0':
                return
            matrix[i][j] = '0'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count

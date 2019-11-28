class Solution(object):
    def uniquePaths(self, grid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m, n = len(grid[0]), len(grid)
        arr = [[0 for _ in range(m)] for _ in range(n)]
        lastrow_flag, lastcol_flag = True, True
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    if i == n - 1:
                        lastrow_flag = False
                    if j == m - 1:
                        lastcol_flag = False
                elif (i == n - 1 and lastrow_flag) or (j == m - 1 and lastcol_flag):
                    arr[i][j] = 1
                elif i < n - 1 and j < m - 1:
                    arr[i][j] = arr[i + 1][j] + arr[i][j + 1]
        print(arr)
        return arr[0][0]


if __name__ == '__main__':
    grid = [[0, 0], [1, 1], [0, 0]]
    print(Solution().uniquePaths(grid))

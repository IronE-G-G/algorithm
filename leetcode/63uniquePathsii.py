"""
63 不同路径ii
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        dp

        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[-1][-1] == 1:
            return 0
        else:
            dp[-1][-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1:
                    if j < n - 1 and obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i][j + 1]
                elif j == n - 1:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i + 1][j]
                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        print(dp)
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    image = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(s.uniquePathsWithObstacles(image))

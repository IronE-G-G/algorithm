"""
62 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

"""

from math import factorial


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        dpij
        状态：ij所在的位置到达终点有多少种路径
        转移：
        dp[i][j]
        i<m-1 and j<n-1:
        dp[i][j] = dp[i+1][j]+dp[i][j+1]
        elif i==m-1:
        dp[i][j] = dp[i][j+1]
        elif j == n-1:
            dp[i][j] == dp[i+1][j]
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]



class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        找规律：
        机器人要向下走m-1，向右走n-1步就能到达终点
        C{m+n-2}^{m-1}
        """
        return factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1))


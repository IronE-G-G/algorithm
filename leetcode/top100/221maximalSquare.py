"""
221 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dpij:以ij为结尾的最大正方形的边长

        matrix[i][j] == 0: dp[i][j]=0
        matrix[i][j] !=0:
        dp[i][j]=min(周围三个的最小值)+1

        ps：可以进行状态压缩

        """
        if not matrix or not matrix[0]:
            return 0
        nrow, ncol = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(ncol)] for i in range(nrow)]

        max_size = max(dp[0] + [dp[i][0] for i in range(1, nrow)])
        for i in range(1, nrow):
            for j in range(1, ncol):
                if dp[i][j] == 0:
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + dp[i][j]
                max_size = max(max_size, dp[i][j])
        return max_size ** 2

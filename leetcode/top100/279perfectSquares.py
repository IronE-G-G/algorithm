"""
279 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        nlogn
        """
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


class Solution1:
    def numSquares(self, n: int) -> int:
        """
        BFS
        """
        queue = {n}
        level = 0
        while queue:
            next_queue = set()
            level += 1
            for item in queue:
                j = 1
                while j * j <= item:
                    if item - j * j == 0:
                        return level
                    next_queue.add(item - j * j)
                    j += 1
            queue = next_queue



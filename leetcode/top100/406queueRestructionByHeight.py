"""
406 根据身高重建队列
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    max_score = 0

    def maxCoins(self, nums: List[int]) -> int:
        """
        1 暴力回溯算法，超时 n！
        2 分治算法，复杂度也是阶乘的形式，但是乘的少一些。
        3 dp ij i-j之间的总分，不含ij
        dp[i][j] = dp[i][k]+d[k][j]+nums[ijk]
        """
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N - 3, -1, -1):
            for j in range(i + 2, N):
                max_score = 0
                for k in range(i + 1, j):
                    max_score = max(max_score, dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
                dp[i][j] = max_score
        return dp[0][-1]





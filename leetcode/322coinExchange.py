"""
322 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else float('inf') for c in coins) + 1
        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]


class Solution:
    res = float('inf')

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dfs+剪枝
        """
        coins.sort(reverse=True)

        def dfs(amount, begin, count):
            if amount == 0:
                self.res = min(self.res, count)
                return
            if begin == len(coins):
                return
            for n in range(amount // coins[begin], -1, -1):
                if count + n >= self.res:
                    # 大的不换换小的硬币数量肯定更多，所以不用往下换了
                    break
                dfs(amount - n * coins[begin], begin + 1, count + n)

        dfs(amount, 0, 0)
        return self.res if self.res < float('inf') else -1


if __name__ == '__main__':
    print(change(103, [1, 2, 6]))

from collections import defaultdict


class Solution:
    """
    求硬币的兑换所有组合
    """

    def change(self, amount, coins) -> int:
        dp = [[]] * (amount + 1)
        dp[0] = [[]]
        for c in coins:
            for i in range(0, amount + 1):
                if i - c >= 0:
                    subres = [item + [c] for item in dp[i - c]]
                    dp[i] = dp[i] + subres
        return dp[-1]



if __name__ == '__main__':
    s = Solution()
    print(s.change(10, [1, 2, 5]))


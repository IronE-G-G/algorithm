class Solution:
    """
    求硬币的组合数
    """

    def change(self, amount, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(0, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.change(10,[1,2,5]))
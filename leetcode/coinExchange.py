def change(amount, coins):
    dp = [[]] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        dp[i] = min(dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
    return dp[-1]


if __name__ == '__main__':
    print(change(103, [1, 2, 6]))

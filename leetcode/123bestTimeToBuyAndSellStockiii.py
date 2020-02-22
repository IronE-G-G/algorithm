class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ndeal = 2
        days = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(1+ndeal)] for _ in range(1+days)]
        for j in range(ndeal+1):
            dp[0][j][1] = float('-inf')
        for i in range(1,days+1):
            dp[i][0][1] = float('-inf')

        for i in range(1, days+1):
            for k in range(1, ndeal+1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i-1])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i-1])
        return dp[-1][-1][0]

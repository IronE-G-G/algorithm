"""
121 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

参考状态机思路：
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/

其他用状态机解决的题：65 有效数字


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        常数dp，维护一个最小价格
        """
        minPrices = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
            minPrices = min(minPrices, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrices)
        return maxProfit


class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        状态机
        dp[i][k][j]:第i天最多买入次数(k),状态(j)为0(非持有)或1(持有)的最大利润
        操作：买入，卖出，无
        初始化：
        dp[0][k][0]=0;dp[0][k][1]=-inf
        dp[i][k][0]=max(dp[i-1][k][1]+prices[i],dp[i-1][k][0])
        dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        """
        k = 1
        days = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(days + 1)]
        for j in range(k + 1):
            dp[0][k][1] = float('-inf')
        for i in range(1, days + 1):
            dp[i][0][1] = float('-inf')

        for i in range(1, days + 1):
            for j in range(1, k + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i - 1])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i - 1])
        return dp[-1][1][0]

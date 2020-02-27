"""
188 买卖股票的最佳时机IV

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        dpkj 当天最多第k笔交易（按买入算），状态j（0为非持有，1为持有）的利润
        初始化
        i=0 状态为1的 -inf
        k=0 状态为1的 -inf
        """
        days = len(prices)
        if k >= days // 2:
            return self.maxProfit_inf(prices)
        k = min(k, days // 2)
        # day0
        pre_dp = [[0 for _ in range(2)] for _ in range(k + 1)]
        for deal_index in range(k + 1):
            pre_dp[deal_index][1] = float('-inf')

        for dayi in range(1, days + 1):
            dp = [[0 for _ in range(2)] for _ in range(k + 1)]
            dp[0][1] = float('-inf')
            for deal_i in range(1, k + 1):
                dp[deal_i][0] = max(pre_dp[deal_i][0], pre_dp[deal_i][1] + prices[dayi - 1])
                dp[deal_i][1] = max(pre_dp[deal_i - 1][0] - prices[dayi - 1], pre_dp[deal_i][1])
            pre_dp = dp
        return pre_dp[k][0]

    def maxProfit_inf(self, prices):
        pre_not_keep, pre_keep = 0, float('-inf')
        for i in range(1, len(prices) + 1):
            now_not_keep = max(pre_keep + prices[i - 1], pre_not_keep)
            now_keep = max(pre_not_keep - prices[i - 1], pre_keep)
            pre_keep, pre_not_keep = now_keep, now_not_keep

        return pre_not_keep

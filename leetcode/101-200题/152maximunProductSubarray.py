"""
152 乘积最大子序列和
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProduct(self, nums) -> int:
        """
        dpi 以第i个为结尾的最大/最小值
        因为只需要前一个，所以是可以压缩一下状态，只存前一个的最大最小值
        """
        if not nums:
            return 0
        max_dp = [0 for _ in range(len(nums))]
        min_dp = [0 for _ in range(len(nums))]
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            min_dp[i] = min(nums[i], nums[i] * min_dp[i - 1], nums[i] * max_dp[i - 1])
            max_dp[i] = max(nums[i], nums[i] * min_dp[i - 1], nums[i] * max_dp[i - 1])
            res = max(max_dp[i], res)
        return res

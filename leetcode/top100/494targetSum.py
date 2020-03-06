"""
494 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
注意:

数组非空，且长度不会超过20。
初始的数组的和不会超过1000。
保证返回的最终结果能被32位整数存下。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        -1~1背包问题 bfs
        """
        if len(nums) == 1:
            return 1 if nums[0] == abs(S) else 0

        pre_lookup = {0: 2} if nums[0] == 0 else {nums[0]: 1, -nums[0]: 1}
        for num in nums[1:]:
            now_lookup = dict()
            for key, value in pre_lookup.items():
                key_add = key + num
                key_sub = key - num

                if key_add not in now_lookup:
                    now_lookup[key_add] = 0
                now_lookup[key_add] += value

                if key_sub not in now_lookup:
                    now_lookup[key_sub] = 0
                now_lookup[key_sub] += value
            pre_lookup = now_lookup

        return 0 if S not in pre_lookup else pre_lookup[S]


class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        -1~1背包问题 dp
        """
        if abs(S) > 1000:
            return 0

        if len(nums) == 1:
            return 1 if nums[0] == abs(S) else 0

        pre_dp = [0 for _ in range(2001)]
        if nums[0] == 0:
            pre_dp[1000] = 2
        else:
            pre_dp[1000 + nums[0]] = 1
            pre_dp[1000 - nums[0]] = 1

        for i in range(1, len(nums)):
            now_dp = [0 for _ in range(2001)]
            for j in range(2001):
                if pre_dp[j] != 0:
                    now_dp[j + nums[i]] += pre_dp[j]
                    now_dp[j - nums[i]] += pre_dp[j]
            pre_dp = now_dp
        return pre_dp[S + 1000]


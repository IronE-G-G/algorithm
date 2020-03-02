"""
300 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划，dpi以元素i为结尾的最长上升子序列长度
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            less_pre_max = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    less_pre_max = max(less_pre_max, dp[j])
            dp[i] = less_pre_max + 1
        return max(dp)


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        维护一个tail表，tail[i]为长度为i+1的最小尾部元素值
        """
        if not nums:
            return 0
        tails = [nums[0]]

        def binary_search(tails, num):
            """
            找第一个大于num的元素下标
            """
            # right的设置
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] == num:
                    return mid
                elif tails[mid] < num:
                    left = mid + 1
                else:
                    # 没有越过去
                    right = mid
            return right

        for i in range(len(nums)):
            target = binary_search(tails, nums[i])
            if target == len(tails):
                tails.append(nums[i])
            else:
                tails[target] = min(tails[target], nums[i])
        return len(tails)

"""
238 除自身以外数组的乘积
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        等于之前的乘积*之后的连乘
        """
        N = len(nums)
        pre_product = [1 for _ in range(N)]
        post_product = [1 for _ in range(N)]

        for i in range(1, N):
            pre_product[i] = pre_product[i - 1] * nums[i - 1]
            post_product[N - i - 1] = post_product[N - i] * nums[N - i]
        return [pre_product[i] * post_product[i] for i in range(N)]


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        来回扫描两遍
        """
        N = len(nums)
        res = [1 for _ in range(N)]
        now = nums[0]
        for i in range(1, N):
            pre = now
            now = now * nums[i]
            res[i] *= pre

        now = nums[-1]
        for i in range(N - 2, -1, -1):
            pre = now
            now = now * nums[i]
            res[i] *= pre
        return res

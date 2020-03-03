"""
560 和为K的数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

类似题目：两数之和，

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        sumj-sumi=k
        把sumi出现的次数存在字典中，如果sumj-k出现在字典中，就增加count
        """
        hashMap = dict()
        hashMap[0] = 1
        sum = 0
        count = 0
        for num in nums:
            sum += num
            if sum - k in hashMap:
                count += hashMap[sum - k]
            if sum not in hashMap:
                hashMap[sum] = 0
            hashMap[sum] += 1
        return count

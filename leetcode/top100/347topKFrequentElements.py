"""
347 前K个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1.数据结构Counter
        2.计数+排序 n~nlogn
        """
        hashMap = dict()
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
        elements = list(hashMap.keys())
        elements.sort(key=lambda x: hashMap[x], reverse=True)
        return elements[:k]


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        3 计数+堆排序 n～nlogk
        """
        import heapq
        hashMap = dict()
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
        return heapq.nlargest(k, hashMap.keys(), key=hashMap.get)

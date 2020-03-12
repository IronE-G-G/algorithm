"""
56 合并区间（中等）
给出一个区间的集合，请合并所有重叠的区间。

实例1：
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        思路：双指针，现对区间进行排序再遍历区间
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        n = len(intervals)
        begin = 0
        end = 1
        res = []
        while end < n:
            beginLeft, beginRight = intervals[begin]
            endLeft, endRight = intervals[end]
            if beginRight >= endLeft:
                intervals[begin][1] = max(beginRight, endRight)
                end += 1
            else:
                res.append(intervals[begin])
                begin = end
                end = begin + 1
        res.append(intervals[begin])
        return res


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1 sort+维护输出结果
        """
        intervals.sort()
        stack = []
        for i in range(len(intervals)):
            if stack and stack[-1][1] >= intervals[i][0]:
                stack[-1][1] = max(stack[-1][1], intervals[i][1])
                continue
            stack.append(intervals[i])
        return stack

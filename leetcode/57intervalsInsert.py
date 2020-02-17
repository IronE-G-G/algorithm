"""
57 插入区间（困难）
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

思路：先找到新区间的位置，再合并区间。
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        insertFlag = False
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                insertFlag = True
                break
        if not insertFlag:
            intervals.append(newInterval)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            ileft, iright = intervals[i]
            if ileft > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(iright, res[-1][1])
        return res

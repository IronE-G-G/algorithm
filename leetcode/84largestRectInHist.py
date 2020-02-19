"""
84 柱状图中最大的句型

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。


"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        寻找以第i个为最短高度的最大矩形面积，即需要寻找第i个元素左右两边第一个小于它的坐标。通过单调栈寻找
        """
        if not heights:
            return 0
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = heights[stack.pop()] * (i - stack[-1] - 1)
                res = max(tmp, res)
            stack.append(i)
        return res

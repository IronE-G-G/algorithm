# -*- coding:utf-8 -*-
"""
滑动窗口的最大值
思路1：维护一个队头为窗口最大值对应下标的队列。
每次移动窗口就判断一下队头是否出界；新加入元素i则判断已经在队列里面的那些元素是否小于元素i，小的话就pop掉。
复杂度是O（n）
暴力法：遍历寻找最大值O（k（n-k））
"""


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size > len(num) or size <= 0:
            return []
        queue, res, i = [], [], 0
        while i < len(num):
            if queue and queue[0] < i - size + 1:
                queue.pop(0)
            while queue and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
            if i >= size - 1:
                res.append(num[queue[0]])
            i += 1
        return res

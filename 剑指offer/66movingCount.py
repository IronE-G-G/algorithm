# -*- coding:utf-8 -*-
"""
机器人的运动范围
思路：bfs
"""


class Solution:
    count = 1

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0:
            return 0
        self.rows = rows
        self.cols = cols
        self.length = rows * cols
        self.flags = [0] * (rows * cols)
        for i in range(rows):
            for j in range(cols):
                digitSum = sum(map(int, str(i) + str(j)))
                if digitSum > threshold:
                    self.flags[i * cols + j] = -1
        self.flags[0] = 1
        self.movingHelper(0)
        return self.count

    def movingHelper(self, ind):
        left = ind - 1
        right = ind + 1
        up = ind - self.cols
        down = ind + self.cols
        for nextItem in [left, right, up, down]:
            if 0 <= nextItem < self.length and self.flags[nextItem] == 0:
                self.flags[nextItem] = 1
                self.count += 1
                self.movingHelper(nextItem)

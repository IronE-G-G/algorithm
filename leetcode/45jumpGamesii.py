"""
45 跳跃游戏ii
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

思路：dp；贪心


1,2,1,1,1
1:[0,1) maxpos = 1
2: [1,2) maxpos = 3
3: [2,4) maxpos = 4
"""
from sys import maxsize


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for _ in range(n)]
        for j in range(n - 2, -1, -1):
            if nums[j] == 0:
                dp[j] = maxsize
            elif nums[j] >= n - j - 1:
                dp[j] = 1
            else:
                dp[j] = 1 + min(dp[(j + 1):(j + 1 + nums[j])])
        return dp[0]


class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        贪心算法
        每一次起跳都预先算一下能到达的最远距离，为下一次的起跳确定一个起跳点的选择区间。
        """
        steps = 0
        begin = 0
        end = 1  # [begin,end) 为可选择的起跳点区间，第一次起跳只能选第0个
        maxPos = 0
        n = len(nums)
        while end < n:
            for i in range(begin, end):
                maxPos = max(maxPos, i + nums[i])
                if i == end - 1:
                    steps += 1
            begin = end
            end = maxPos + 1
        return steps


if __name__ == '__main__':
    s = Solution2()
    print(s.jump([1, 2, 1, 1, 1]))

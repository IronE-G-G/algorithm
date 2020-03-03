from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        双向队列
        维护一个单调递减队列，加入当前元素之前，从后往前遍历队列，把小于该元素的pop掉。
        如果当前window的第一个元素等于当前队列的第一个元素，则出掉当前队列的第一个元素。
        python里面的队列：from Queue import queue 操作是put，get
        """
        windows = deque()
        res = []
        for i in range(len(nums)):
            while windows and windows[-1] < nums[i]:
                windows.pop()
            windows.append(nums[i])
            if i < k - 1:
                continue
            res.append(windows[0])
            if nums[i - k + 1] == windows[0]:
                windows.popleft()
        return res


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        把nums按每块k个分割，每一次滑动窗口最多在两块之间，那么如果知道i到右边界的最大值以及j到左边界的最大值，那么就能知道这个滑动窗口的最大值了。
        dp
        """
        N = len(nums)
        left_max = [0 for _ in range(N)]
        right_max = [0 for _ in range(N)]

        for i in range(N):
            if i % k == 0:
                maximum = float('-inf')

            maximum = max(maximum, nums[i])
            left_max[i] = maximum

        maximum = float('-inf')
        for i in range(N - 1, -1, -1):
            maximum = max(maximum, nums[i])
            right_max[i] = maximum
            if i % k == 0:
                maximum = float('-inf')

        res = []
        for j in range(N):
            if j < k - 1:
                continue
            res.append(max(right_max[j - k + 1], left_max[j]))
        return res

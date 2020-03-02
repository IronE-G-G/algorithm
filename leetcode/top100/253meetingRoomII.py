"""
253 会议室ii
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        优先队列，复杂度为On2
        """
        intervals.sort()
        priority_queue = []
        for item in intervals:
            free = False
            for i, end in enumerate(priority_queue):
                if end <= item[0]:
                    priority_queue[i] = item[1]
                    free = True
                    break
            if not free:
                priority_queue.append(item[1])
        return len(priority_queue)


class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        维护小顶堆
        :param intervals:
        :return:
        """
        if not intervals:
            return 0
        import heapq
        intervals.sort()
        mini_heap = []
        heapq.heappush(mini_heap, intervals[0][1])
        for item in intervals[1:]:
            if item[0] >= mini_heap[0]:
                heapq.heapreplace(mini_heap, item[1])
            else:
                heapq.heappush(mini_heap, item[1])
        return len(mini_heap)

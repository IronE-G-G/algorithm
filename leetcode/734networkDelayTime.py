"""
734 网络延迟问题
有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

注意:

N 的范围在 [1, 100] 之间。
K 的范围在 [1, N] 之间。
times 的长度在 [1, 6000] 之间。
所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/network-delay-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Dijkstra 算法 路径非负，单节点到其他所有节点的最短路径
        1 初始化图 用嵌套的字典来构建
        2 初始化K到其他点的距离，用字典来构建
        3 找到第一个最小距离的到达点，如果这个点到点V的距离加上K到这个点的距离比K到V的距离短，则更新
        """
        # graph init
        graph = dict()
        for start, end, cost in times:
            if start not in graph:
                graph[start] = dict()
            graph[start][end] = cost
        if K not in graph:
            return -1
        # 最后要求的结果
        max_dist = float('-inf')

        # K to other points'distance
        distance = {end: graph[K].get(end, float('inf')) for end in range(1, N + 1)}
        destination = set([i for i in range(1, N + 1) if i != K])
        # 找距离最短的到达点
        while destination:
            min_dist, corr_end = float('inf'), None
            for end in destination:
                if end in distance and distance[end] < min_dist:
                    min_dist = distance[end]
                    corr_end = end
            # 不存在，返回
            if corr_end is None:
                return -1
            # 移除最小点
            destination.remove(corr_end)
            # 更新结果，这样就不用算法完成的时候再去遍历一遍distance然后取最大值
            max_dist = max(max_dist, min_dist)
            # 找到一个最小点，更新distance
            if corr_end in graph:
                for end, cost in graph[corr_end].items():
                    if min_dist + graph[corr_end][end] < distance[end]:
                        distance[end] = min_dist + graph[corr_end][end]
        return max_dist


class Solution1:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        floyd 算法
        dp 初始状态：dpij直达的最小距离
        1-K-N，dpij 最多中间经过前K个节点的最小距离
        """
        dp = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
        for start, end, cost in times:
            dp[start][end] = cost
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
        min_dist = dp[K]
        min_dist.pop(K)
        min_dist.pop(0)
        res = max(min_dist)
        if res == float('inf'):
            return -1
        return res

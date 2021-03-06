"""
207 课程表
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        查找一个循环是否存在于有向图中,使用拓扑排序
        拓扑排序：统计所有点的入度，如果点的入度为0，则加入到队列中，
        如果队列不为空
        出队，元素的所有出度点的入度-1

        拓扑排序的题目：210 课程表ii
        """
        if not prerequisites:
            return True
        # 统计元素的入度
        in_degree = [0 for _ in range(numCourses)]
        # 记录元素的出度元素列表
        out_degree = dict()
        # 记录未出队的元素
        courses = set([i for i in range(numCourses)])

        # 初始化
        for begin, end in prerequisites:
            if begin not in out_degree:
                out_degree[begin] = []
            out_degree[begin] += [end]
            in_degree[end] += 1
            courses.add(begin)
            courses.add(end)
        # 记录入度为0的元素，可以出队
        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        # BFS
        while queue:
            queue_next = []
            for item in queue:
                courses.remove(item)
                if item not in out_degree:
                    continue
                for dependency in out_degree[item]:
                    in_degree[dependency] -= 1
                    if in_degree[dependency] == 0:
                        queue_next.append(dependency)
            queue = queue_next
        return not courses

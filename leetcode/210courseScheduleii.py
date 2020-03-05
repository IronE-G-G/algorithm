"""
210 课程表ii
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        拓扑排序，收集入度为0的元素
        """
        in_degree = [0 for _ in range(numCourses)]
        out_degree_list = dict()
        courses = set([i for i in range(numCourses)])
        res = []
        # init
        for start, end in prerequisites:
            if start not in out_degree_list:
                out_degree_list[start] = []
            out_degree_list[start].append(end)
            in_degree[end] += 1

        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        while queue:
            queue_next = []
            res = queue + res
            for course in queue:
                courses.remove(course)
                if course not in out_degree_list:
                    continue
                for dependency in out_degree_list[course]:
                    in_degree[dependency] -= 1
                    if in_degree[dependency] == 0:
                        queue_next.append(dependency)
            queue = queue_next
        return res if not courses else []

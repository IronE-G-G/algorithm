"""
399 除法求值
给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Floyd算法
        """
        hashMap = dict()
        count = 0
        for dividend, divisor in equations:
            if dividend not in hashMap:
                hashMap[dividend] = count
                count += 1
            if divisor not in hashMap:
                hashMap[divisor] = count
                count += 1

        dp = [[None for _ in range(count)] for _ in range(count)]
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            dividend = hashMap[dividend]
            divisor = hashMap[divisor]
            dp[dividend][divisor] = values[i]
            dp[divisor][dividend] = 1 / values[i]

        # 三层循环不能写反
        for k in range(count):
            for i in range(count):
                for j in range(count):
                    if j == i:
                        dp[i][j] = 1.0
                    if dp[i][j] is not None:
                        continue
                    if k == i or k == j:
                        continue
                    if dp[i][k] is not None and dp[k][j] is not None:
                        dp[i][j] = dp[i][k] * dp[k][j]

        results = []
        for dividend, divisor in queries:
            if dividend not in hashMap or divisor not in hashMap:
                results.append(-1.0)
                continue
            res = -1.0
            dividend = hashMap[dividend]
            divisor = hashMap[divisor]
            if dp[dividend][divisor] is not None:
                res = dp[dividend][divisor]
            results.append(res)
        return results


class Solution1:
    visited = set()

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        图+DFS
        """
        graph = dict()
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            if dividend not in graph:
                graph[dividend] = dict()
            graph[dividend][divisor] = values[i]
            if divisor not in graph:
                graph[divisor] = dict()
            graph[divisor][dividend] = 1 / values[i]

        def dfs(begin, end):
            if begin not in graph or end not in graph:
                return -1
            if begin == end:
                return 1
            if end in graph[begin]:
                return graph[begin][end]
            for node in graph[begin]:
                if node in self.visited:
                    continue
                self.visited.add(node)
                post_res = dfs(node, end)
                if post_res != -1:
                    return post_res * graph[begin][node]
            return -1

        res = []
        for begin, end in queries:
            self.visited.clear()
            self.visited.add(begin)
            res.append(dfs(begin, end))
        return res


class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        图+BFS
        """
        graph = dict()
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            if dividend not in graph:
                graph[dividend] = dict()
            graph[dividend][divisor] = values[i]
            if divisor not in graph:
                graph[divisor] = dict()
            graph[divisor][dividend] = 1 / values[i]

        def bfs(begin, end):
            if begin not in graph or end not in graph:
                return -1
            if begin == end:
                return 1
            if end in graph[begin]:
                return graph[begin][end]
            visited = set()
            queue = {begin: 1}
            while queue:
                queue_next = {}
                for start in queue:
                    for dest in graph[start]:
                        if dest in visited:
                            continue
                        visited.add(dest)
                        if dest == end:
                            return queue[start] * graph[start][dest]
                        queue_next[dest] = queue[start] * graph[start][dest]
                queue = queue_next
            return -1

        res = []
        for begin, end in queries:
            res.append(bfs(begin, end))
        return res

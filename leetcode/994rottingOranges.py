"""
994 腐烂的橘子
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotting-oranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS
        """
        nrow, ncol = len(grid), len(grid[0])
        queue = [(i, j) for i in range(nrow) for j in range(ncol) if grid[i][j] == 2]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minute = 0
        while True:
            next_queue = []
            for item in queue:
                neighbors = [(item[0] + d[0], item[1] + d[1]) for d in directions]
                for i, j in neighbors:
                    if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] != 1:
                        continue

                    grid[i][j] = 2
                    next_queue.append((i, j))
            if not next_queue:
                break
            queue = next_queue
            minute += 1
        return minute if all([1 not in grid[i] for i in range(nrow)]) else -1

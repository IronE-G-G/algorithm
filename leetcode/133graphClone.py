"""
133 克隆图
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}
 

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1，第二个节点值为 2，以此类推。该图在测试用例中使用邻接列表表示。

邻接列表是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/clone-graph
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        BFS
        """
        if not node:
            return None
        if not node.neighbors:
            return Node(node.val)

        built = dict()
        done = set()
        queue = {node}

        while queue:
            next_queue = set()
            for root in queue:
                val = root.val
                # 节点的邻接点是否已经配置
                if val in done:
                    continue
                # 节点是否已经建立
                if val in built:
                    clone = built[val]
                else:
                    clone = Node(val)
                    built[val] = clone
                # 配置邻接点
                candidates = []
                for item in root.neighbors:
                    if item.val not in built:
                        cloneItem = Node(item.val)
                        built[item.val] = cloneItem
                    else:
                        cloneItem = built[item.val]
                    candidates.append(cloneItem)
                    next_queue.add(item)

                clone.neighbors = candidates
                done.add(val)
            queue = next_queue

        return built[node.val]


class Solution1(object):
    visited = dict()

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        DFS

        """
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        clone = Node(node.val)
        self.visited[node] = clone
        candidates = [self.cloneGraph(item) for item in node.neighbors]
        clone.neighbors = candidates
        return clone

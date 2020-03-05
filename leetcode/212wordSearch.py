"""
212 单词搜索ii
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self):
        self.links = dict()
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.links:
                cur.links[char] = TreeNode()
            cur = cur.links[char]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        tree = Trie()
        for word in words:
            tree.insert(word)

        res = set()

        def dfs(i, j, root, path):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in root.links:
                return
            char = board[i][j]
            path = path + [char]
            # 访问过的用-代替掉，等这个dfs完了再补回来
            board[i][j] = '-'
            if root.links[char].isEnd:
                res.add(''.join(path))

            dfs(i + 1, j, root.links[char], path)
            dfs(i - 1, j, root.links[char], path)
            dfs(i, j - 1, root.links[char], path)
            dfs(i, j + 1, root.links[char], path)
            # 恢复原来的值
            board[i][j] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, tree.root, [])
        return list(res)

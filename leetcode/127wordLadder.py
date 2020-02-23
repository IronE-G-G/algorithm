"""
127 单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。

"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        BFS
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        neighbors = dict()

        def findNeighbors(word):
            if word in neighbors:
                return neighbors[word]
            candidates = []
            for i in range(len(word)):
                for exchangej in range(ord('a'), ord('z') + 1):
                    candidate = word[:i] + chr(exchangej) + word[(i + 1):]
                    if candidate in wordList:
                        candidates.append(candidate)
            neighbors[word] = candidates
            return candidates

        queue = [beginWord]
        level = 1
        visited = set([beginWord])
        while queue:
            level += 1
            next_queue = []
            for word in queue:
                candidates = findNeighbors(word)
                for candidate in candidates:
                    if candidate == endWord:
                        return level
                    if candidate not in visited:
                        visited.add(candidate)
                        next_queue.append(candidate)
            queue = next_queue
        return 0


class Solution1(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        双向BFS
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        neighbors = dict()

        # 寻找邻接点
        def findNeighbors(word):
            if word in neighbors:
                return neighbors[word]
            candidates = []
            for i in range(len(word)):
                for exchangej in range(ord('a'), ord('z') + 1):
                    candidate = word[:i] + chr(exchangej) + word[(i + 1):]
                    if word[i] != chr(exchangej) and candidate in wordList:
                        candidates.append(candidate)
            neighbors[word] = candidates
            return candidates

        beginWord_queue, endWord_queue = [beginWord], [endWord]
        # 记录每一层用过的单词
        begin_levels = {1: [beginWord]}
        end_levels = {1: [endWord]}
        # 记录begin和end所有用过的单词
        begin_visited, end_visited = set([beginWord]), set([endWord])

        # 寻在单词在一个层次遍历中的层数（已知单词在这个层次遍历序列中了）
        def findInLevel(word, level_dict):
            for i in range(1, len(level_dict) + 1):
                words = level_dict[i]
                if word in words:
                    return i

        # 双向BFS，先开始begin端
        while beginWord_queue and endWord_queue:
            next_queue = []
            for word in beginWord_queue:

                candidates = findNeighbors(word)
                for candidate in candidates:
                    # 单词在end端出现，返回begin端完整遍历层数+单词在end端的层
                    if candidate in end_visited:
                        return len(begin_levels) + findInLevel(candidate, end_levels)
                    if candidate in begin_visited:
                        continue
                    begin_visited.add(candidate)
                    next_queue.append(candidate)
            begin_levels[len(begin_levels) + 1] = next_queue
            beginWord_queue = next_queue
            # 交换让end端BFS
            beginWord_queue, endWord_queue = endWord_queue, beginWord_queue
            begin_levels, end_levels = end_levels, begin_levels
            begin_visited, end_visited = end_visited, begin_visited

        return 0

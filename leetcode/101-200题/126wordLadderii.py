"""
126 单词接龙ii
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    leetcode python3 编辑器
    BFS
    """
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        queue = [[beginWord, [beginWord]]]
        levelWords = set([beginWord])
        res = []
        stopFlag = False
        # hashtable to store neighbor node
        hashTable = dict()
        while queue:
            nextQueue = []
            nowLevelWords = set()
            for i in range(len(queue)):
                word, path = queue[i]
                if word == endWord:
                    stopFlag = True
                    res.append(path)
                    continue

                candidates = []
                if word in hashTable:
                    candidates = hashTable[word]

                for ichar in range(len(word)):
                    for exchangej in range(ord('a'), ord('z') + 1):
                        candidate = word[:ichar] + chr(exchangej) + word[(ichar + 1):]
                        if word[ichar] != chr(exchangej) and candidate in wordList:
                            candidates.append(candidate)

                for candidate in candidates:
                    if candidate not in levelWords:
                        nowLevelWords.add(candidate)
                        nextQueue.append([candidate, path + [candidate]])
            if stopFlag:
                return res

            queue = nextQueue
            levelWords.update(nowLevelWords)

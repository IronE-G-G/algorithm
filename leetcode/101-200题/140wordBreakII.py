"""
140 单词拆分ii
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        N = len(s)
        splitable = [False for _ in range(N)]
        self.size = set([len(item) for item in wordDict])
        wordDict = set(wordDict)
        for i in range(N - 1, -1, -1):
            if s[i:] in wordDict:
                splitable[i] = True
                continue
            for j in range(i + 1, N):
                if splitable[j] and s[i:j] in wordDict:
                    splitable[i] = True
                    break

        if not splitable[0]:
            return []
        res = []

        def backtrack(s, start, path):
            if not s:
                res.append(' '.join(path))
                return
            for i in [item for item in self.size if item <= len(s)]:
                if s[:i] in wordDict and (start + i >= len(splitable) or splitable[start + i]):
                    backtrack(s[i:], start + i, path + [s[:i]])

        backtrack(s, 0, [])
        return res

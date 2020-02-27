"""
30 串联所有单词子串（困难）
给定一个字符串 s 和一些长度相同的单词 words。
找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

思路：滑窗+分割窗口统计单词是否相同
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if not s or not words:
            return []
        wordset = Counter(words)
        res = []
        N = len(s)
        wordLen = len(words[0])
        matchN = len(words) * len(words[0])
        for index in range(0, N - matchN + 1):
            sub = s[index:(index + matchN)]
            candidate = []
            for i in range(0, matchN, wordLen):
                candidate.append(sub[i:(i + wordLen)])
            candidate = Counter(candidate)
            if candidate == wordset:
                res.append(index)
        return res

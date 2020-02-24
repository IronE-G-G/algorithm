"""
139 单词拆分

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        dpi 前i个元素为结尾的子串是否能拆分
        """
        if not wordDict:
            return False
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        回溯 dfs
        复杂度为n**n
        最大的例子时会超时

        """
        if not wordDict:
            return False
        self.size = set([len(item) for item in wordDict])
        self.min_size = min(self.size)
        self.res = False
        wordDict = set(wordDict)

        def backtrack(s):
            if not s:
                self.res = True
                return
            if len(s) < self.min_size:
                return

            for i in [item for item in self.size if item <= len(s)]:
                if s[:i] in wordDict:
                    backtrack(s[i:])

        backtrack(s)
        return self.res


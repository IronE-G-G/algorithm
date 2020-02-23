"""
131 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        dpij:[i,j]范围是不是回文
        从后往前遍历更新
        """
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if i == j:
                    dp[i][j] = True
                elif j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

        res = []

        def backtrack(rest, begin, path):
            if not rest:
                res.append(path)
                return
            for i in range(len(rest)):
                if dp[begin][begin + i]:
                    backtrack(rest[(i + 1):], begin + i + 1, path + [rest[:(i + 1)]])

        backtrack(s, 0, [])
        return res

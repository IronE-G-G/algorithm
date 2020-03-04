"""
647 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        dpij 从i到j是不是回文
        i>j+1
        dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
        """
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        count = N
        for i in range(N - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, N):
                if j == i + 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]:
                    count += 1
        return count


class Solution1:
    def countSubstrings(self, s: str) -> int:
        """
        中心扩展法
        """
        res = 0
        N = len(s)
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

"""
10 正则化表达式匹配（困难）

keyword：字符串，回溯法，动态规划
"""


class Solution1:
    """
    回溯法
    """

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        # 首字母是否匹配
        firstMatch = s and (p[0] == '.' or s[0] == p[0])
        if len(p) >= 2 and p[1] == '*':
            # 分x*不匹配字母；x*匹配字母两种情况，x*只有不匹配的时候才会被跳过
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])


class Solution2:
    """
    动态规划：
    状态：
    dp[i][j]为s[:i] p[:j]是否匹配

    """
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp = len(s), len(p)
        dp = [[False] * (lenp + 1) for i in range(lens + 1)]
        # p和s同时为空
        dp[0][0] = True
        for i in range(lens + 1):
            for j in range(1, lenp + 1):
                # s为空的情况下根据p的取值有可能为True
                if i == 0:
                    if j > 1 and p[j - 1] == '*':
                        dp[0][j] = dp[0][j - 2]
                else:
                    if j > 1 and p[j - 1] == '*':
                        firstMatch = s[i - 1] == p[j - 2] or p[j - 2] == '.'
                        dp[i][j] = dp[i][j - 2] or (firstMatch and dp[i - 1][j])
                    else:
                        firstMatch = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                        dp[i][j] = firstMatch and dp[i - 1][j - 1]
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution2()
    print(solution.isMatch('aa', 'a*'))

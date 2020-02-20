"""
87 扰动字符串

如果s2是s1的扰动字符串：
len(s1) == len(s2)
s1的字母组成跟s2的字母组成一样
存在分隔点i，将s1分隔成T1，T2；将s2分割成T3，T4
那么T1～T3 and T2～T4
或者 T1～T4 and T2～T3
～代表扰动或等于
"""
from collections import Counter


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        递归+剪枝

        """
        if not s1 and not s2:
            return True
        if len(s1) != len(s2):
            return False
        if Counter(s1) != Counter(s2):
            return False
        return self.helper(s1, s2)

    def helper(self, word1, word2):
        if len(word1) == 1:
            if word1[0] == word2[0]:
                return True
            else:
                return False
        for i in range(1, len(word1)):
            if Counter(word1[:i]) == Counter(word2[:i]) and Counter(word1[i:]) == Counter(word2[i:]) and self.helper(
                    word1[:i], word2[:i]) and self.helper(word1[i:], word2[i:]):
                return True
            if Counter(word1[:i]) == Counter(word2[-i:]) and Counter(word1[i:]) == Counter(word2[:-i]) and self.helper(
                    word1[:i], word2[-i:]) and self.helper(word1[i:], word2[:-i]):
                return True
        return False


class Solution1(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        dp[i][j][len]：s1第i个起的len个跟s2第j个起的len个是否为扰动字符串
        状态转移：
        存在分割点使得s1（T1+T2）和s2（T3+T4）的两个子串互为扰动字符串
        T1～T3，T2～T4 or T1～T4，T2～T3
        """
        if not s1 and not s2:
            return True
        if len(s1) != len(s2):
            return False
        if len(s1) == 1:
            return s1 == s2
        lens = len(s1)
        dp = [[[False for _ in range(lens + 1)] for _ in range(lens)] for _ in range(lens)]
        for i in range(lens):
            for j in range(lens):
                dp[i][j][1] = s1[i] == s2[j]

        for k in range(2, lens + 1):
            for i in range(lens - k + 1):
                for j in range(lens - k + 1):
                    for len1 in range(1, k):
                        if dp[i][j][len1] and dp[i + len1][j + len1][k - len1] or (
                                dp[i][j + k - len1][len1] and dp[i + len1][j][k - len1]):
                            dp[i][j][k] = True
                            break
        return dp[0][0][lens]


if __name__ == '__main__':
    s = Solution1()
    print(s.isScramble('abc', 'abc'))

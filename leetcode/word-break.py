class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        if s in wordDict:
            return True
        dp = [True]
        for right in range(0, len(s)):
            res = False
            for sep in range(right, -1, -1):
                rightPart = s[sep:(right+1)]
                leftPart = dp[sep]
                if rightPart in wordDict and leftPart:
                    res = True
                    break
            dp.append(res)
        return dp[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ['leet','code']
    print(Solution().wordBreak(s, wordDict))

"""
32 最常有效括号（难）
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

"""


class Solution1(object):
    """
    暴力法，检查每个偶数长的子串
    """
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        count = lens // 2
        res = 0
        for i in range(1, count + 1):
            step = 2 * i
            for index in range(0, lens - step + 1):
                if self.substringCheck(s[index:(index + step)]):
                    res = step
                    break
        return res

    def substringCheck(self, s):
        left = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                left -= 1
            if left < 0:
                return False
        return left == 0


class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        动态规划
        状态：元素i为以坐标i结尾的最长字符子串的长度，i为（的则长度为0
        状态转移：
        s[i]=')' and s[i-1]='(':
            =====> dp[i] = dp[i-2]+2
        s[i]=')' and s[i-1]=')' ans s[i-dp[i-1]-1]='(' :
            =====> dp[i] = dp[i-dp[i-1]-2]+dp[i-1]+2

        """
        if not s:
            return 0
        lens = len(s)
        dp = [0] * lens
        for i in range(1, lens):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # （）形式时i-2取到最后一个dp元素的默认值0，因此不必处理
                    dp[i] = dp[i - 2] + 2
                else:
                    pre = i - dp[i - 1] - 1
                    if pre >= 0 and s[pre] == '(':
                        # 边界值同为默认值0
                        dp[i] = dp[pre - 1] + dp[i - 1] + 2
        return max(dp)


class Solution3(object):
    def longestValidParentheses(self, s):
        """
        栈方法，有效括号符合先进后出的规则。用栈存储有效子串的分隔下标
        """
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res







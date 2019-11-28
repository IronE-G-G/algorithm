class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        self.maxlen = 1
        self.res = s[0]
        self.s = s
        self.slen = len(s)
        for i in range(len(s)):
            self.centerExpand(i, i)
            if i < len(s) - 1 and s[i] == s[i + 1]:
                self.centerExpand(i, i + 1)
                if self.maxlen < 2:
                    self.maxlen = 2
                    self.res = s[i:(i + 2)]

        return self.res

    def centerExpand(self, ind1, ind2):
        for offset in range(1, ind1 + 1):
            left = ind1 - offset
            right = ind2 + offset
            if left < 0 or right >= self.slen or self.s[left] != self.s[right]:
                break
            else:
                if right - left + 1 > self.maxlen:
                    self.res = self.s[left:(right + 1)]
                    self.maxlen = right - left + 1
                    print(left, right, self.res)


class Solution1(object):
    def longestPalindrome(self, s):
        slen = len(s)
        maxlen = 1
        res = s[0]
        arr = [[False for _ in range(slen)] for _ in range(slen)]
        for right in range(1,slen):
            for left in range(right):
                if s[left]==s[right] and ((right-left<=2) or arr[left+1][right-1]):
                    arr[left][right] = True
                    if right-left+1>maxlen:
                        maxlen = right-left+1
                        res = s[left:(right+1)]
        return res




if __name__ == '__main__':
    s = "dddddd"
    print(Solution1().longestPalindrome(s))

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == '0':
            return 0
        N = len(s)
        results = [1 for _ in range(N+1)]
        if s[N-1] == '0':
            results[N-1] = 0
        for i in range(N - 2, -1, -1):
            if s[i] == '0':
                results[i] = 0
            elif int(s[i:(i + 2)]) <= 26:
                results[i] = results[i + 1] + results[i + 2]
            elif int(s[i:(i + 2)]) > 26:
                results[i] = results[i+1]
        return results[0]


if __name__ == '__main__':
    print(Solution().numDecodings('12'))

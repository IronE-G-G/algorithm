"""
93 复原ip地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]


"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) < 4 or len(s) > 12:
            return []

        def backtrack(string, path):
            if not string:
                if len(path) == 4:
                    res.append('.'.join(path))
                return
            if string[0] == '0':
                backtrack(string[1:], path + ['0'])
                return
            for i in range(1, min(3, len(string)) + 1):
                if 0 < int(string[:i]) <= 255 and (4 - len(path) - 1) <= len(string[i:]) <= 3 * (4 - len(path) - 1):
                    backtrack(string[i:], path + [string[:i]])

        backtrack(s, [])
        return res

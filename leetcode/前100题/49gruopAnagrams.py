"""
49 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

思路：哈希表
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        strs.sort()
        for string in strs:
            sortedStr = ''.join(sorted(string))
            if sortedStr in table:
                table[sortedStr].append(string)
            else:
                table[sortedStr] = [string]
        return list(table.values())

"""
无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

思路1:用i标记子串的起始位置，j从起始位置开始遍历。如果遇到重复的，则i移动到字典中重复字符所在位置的后一位（回溯）
边界处理：j遍历完的时候要终止while。

思路2：思路1中需要改进的地方是回溯后重复计算的部分，回溯重复计算的部分出了重复字符的位置改变外其他字符都没有改变。
这里用i来指示子串的左边界（子串不包含i），如果遇到重复则改变位置i，同时在整体的字典中更新重复字符的位置。

"""


class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = 0
        length = len(s)
        maxCount = 0
        while i < length:
            uniqueSet = dict()
            count = 0
            for j in range(i, length):
                if s[j] not in uniqueSet:
                    uniqueSet[s[j]] = j
                    count += 1
                    maxCount = max(maxCount, count)
                else:
                    maxCount = max(maxCount, count)
                    i = uniqueSet[s[j]] + 1
                    break
            if j == length - 1:
                break
        return maxCount


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = len(s)
        i = -1
        uniqueSet = dict()
        maxCount = 0
        for j in range(length):
            if s[j] in uniqueSet:
                # 如果重复了，则检查重复字符所在位置是否大于i，大于的话则i指向重复字符所在位置
                i = max(i, uniqueSet[s[j]])
            maxCount = max(maxCount, j - i)
            uniqueSet[s[j]] = j
        return maxCount

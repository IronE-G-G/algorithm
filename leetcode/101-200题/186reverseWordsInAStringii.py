"""
186 翻转字符串里的单词ii
给定一个字符串，逐个翻转字符串中的每个单词。

示例：

输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
注意：

单词的定义是不包含空格的一系列字符
输入字符串中不会包含前置或尾随的空格
单词与单词之间永远是以单个空格隔开的
进阶：使用 O(1) 额外空间复杂度的原地解法。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        句子翻转+单词翻转
        """
        if not s:
            return None
        s.append(' ')
        left, right = 0, 0
        # word reverse
        while right < len(s):
            if s[right] != ' ':
                right += 1
                continue
            cur = right - 1
            while left < cur:
                s[left], s[cur] = s[cur], s[left]
                cur -= 1
                left += 1
            right += 1
            left = right
        # sentence reverse
        s.pop()
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

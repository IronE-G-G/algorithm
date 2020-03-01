"""
394 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

膜拜一下大佬代码优雅的栈方法
https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        栈方法，
        两个栈一个记录数字一个记录左右括号
        """
        num_stack = []
        parenthese_stack = []
        i = 0
        while True:
            if i == len(s):
                return s
            char = s[i]
            if char == '[':
                parenthese_stack.append(i)
            elif '0' <= char <= '9':
                if i > 0 and '0' <= s[i - 1] <= '9':
                    i += 1
                    continue
                num_stack.append(i)
            elif char == ']':
                num_begin = num_stack.pop()
                left_parenthese = parenthese_stack.pop()
                prev = s[:num_begin] + int(s[num_begin:left_parenthese]) * s[left_parenthese + 1:i]
                s = prev + s[i + 1:]
                i = len(prev) - 1
            i += 1

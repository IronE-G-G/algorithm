"""
68 文本左右对齐（困难）
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]

        """
        res = []

        def helper(maxWidth):
            candidates = []
            nChars = 0
            spaces = 0

            # 找单词部分
            while words:
                nextWord = words[0]
                wordLen = len(nextWord)
                if nChars + wordLen <= maxWidth:
                    candidates.append(nextWord)
                    nChars = nChars + wordLen
                    words.pop(0)
                    if candidates:
                        nChars += 1
                else:
                    spaces = maxWidth + 1 - nChars
                    break

            # 单词拼接
            # 最后一行左对齐
            if not words:
                row = ' '.join(candidates)
                row += ' ' * (maxWidth - len(row))
                res.append(row)
            # 只有一个单词的也左对齐
            elif len(candidates) == 1:
                res.append(candidates[0] + ' ' * spaces)
                helper(maxWidth)
            # 空格分配
            else:
                distance = spaces // (len(candidates) - 1)
                rest = spaces % (len(candidates) - 1)
                gaps = [distance + 1 for _ in range(len(candidates) - 1)]
                gaps.append(0)
                row = ''
                for i in range(len(candidates)):
                    row = row + candidates[i] + ' ' * gaps[i]
                    if i < rest:
                        row += ' '
                res.append(row)
                helper(maxWidth)

        helper(maxWidth)
        return res

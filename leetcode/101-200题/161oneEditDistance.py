"""
161 相隔为1的编辑距离
给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

注意：

满足编辑距离等于 1 有三种可能的情形：

往 s 中插入一个字符得到 t
从 s 中删除一个字符得到 t
在 s 中替换一个字符得到 t
示例 1：

输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if abs(len(s) - len(t)) > 1:
            return False
        # lent>=lens
        for i in range(min(len(s), len(t))):
            if s[i] == t[i]:
                continue
            return s[i:] == t[(i + 1):] or s[(i + 1):] == t[i:] or s[(i + 1):] == t[(i + 1):]
        return len(s) != len(t)

"""
125 验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        左右指针
        """
        if not s:
            return True
        left, right = 0, len(s) - 1
        s = s.lower()
        while left <= right:
            while left <= right and not ('0' <= s[left] <= '9' or 'a' <= s[left] <= 'z'):
                left += 1
            while left <= right and not ('0' <= s[right] <= '9' or 'a' <= s[right] <= 'z'):
                right -= 1
            if left > right:
                break
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

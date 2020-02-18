"""
65 有效数字


"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        有限自动机,如65ValidNum.jpg所示
        """
        s = s.strip()
        finalState = [2, 4, 6, 8]
        transferTable = [
            [1, 2, -1, 3],
            [-1, 2, -1, 3],
            [-1, 2, 5, 8],
            [-1, 4, -1, -1],
            [-1, 4, 5, -1],
            [7, 6, -1, -1],
            [-1, 6, -1, -1],
            [-1, 6, -1, -1],
            [-1, 8, 5, -1]]
        state = 0
        for char in s:
            if char in '+-':
                state = transferTable[state][0]
            elif '0' <= char <= '9':
                state = transferTable[state][1]
            elif char == 'e':
                state = transferTable[state][2]
            elif char == '.':
                state = transferTable[state][3]
            else:
                return False
            if state == -1:
                return False

        return state in finalState


class Solution1(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        sign,pointStart,expStart,numStart
        首字母可以为符号，0-9，小数点
        为符号：保证后面为数字或（小数点+数字）
        为小数点：保证后面为数字

        从没检查过的char开始
        if 0<=char<=9: pass
        if char == 'e': 保证前面没用过e并且前一个字符为数字或者小数点；后一个字符为数字或者（符号+数字）

        if char == '.' 前一个字符为数字；e没有用过；小数点没用过
        if char in '+-'：前一个字符为e；后一个为数字
        """
        s = s.strip()
        if not s:
            return False

        pointStart = False
        expStart = False
        start = 1
        if '0' <= s[0] <= '9':
            pass
        elif s[0] in '+-' and len(s) > 1:
            if '0' <= s[1] <= '9':
                pass
            elif s[1] == '.' and len(s) > 2 and '0' <= s[2] <= '9':
                pointStart = True
                start = 2
        elif s[0] == '.' and len(s) > 1 and '0' <= s[1] <= '9':
            pointStart = True
        else:
            return False

        for i in range(start, len(s)):
            if '0' <= s[i] <= '9':
                continue
            elif s[i] == 'e' and not expStart and ('0' <= s[i - 1] <= '9' or s[i - 1] == '.') and i < len(s) - 1 and (
                    '0' <= s[i + 1] <= '9' or s[i + 1] in '+-'):
                expStart = True
            elif s[i] == '.' and '0' <= s[i - 1] <= '9' and not expStart and not pointStart:
                pointStart = True
            elif s[i] in '+-' and s[i - 1] == 'e' and i < len(s) - 1 and '0' <= s[i + 1] <= '9':
                continue
            else:
                return False
        return True

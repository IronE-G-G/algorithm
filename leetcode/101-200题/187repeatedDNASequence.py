"""
187 重复的DNA序列
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。

 

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        哈希表
        将字符映射到int上减少空间消耗
        """
        res = set()
        visited = set()
        if len(s) <= 10:
            return []
        hashMap = dict()
        hashMap['A'] = 0
        hashMap['C'] = 1
        hashMap['G'] = 2
        hashMap['T'] = 3
        begin = 0
        base = 0xfffff
        for i in range(0, len(s)):
            begin = (begin << 2) & base | hashMap[s[i]]
            if i < 9:
                continue
            if begin in visited:
                res.add(s[(i - 9):(i + 1)])
            else:
                visited.add(begin)
        return list(res)

        return list(res)

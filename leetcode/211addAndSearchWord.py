"""
211 添加与搜索单词-数据结构设计
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self):
        self.links = dict()
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for char in word:
            if char not in cur.links:
                cur.links[char] = TreeNode()
            cur = cur.links[char]
        cur.isEnd = True

    def search(self, word: str, cur=None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not cur:
            cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char != '.' and char not in cur.links:
                return False
            if char != '.':
                cur = cur.links[char]
            else:
                for char in cur.links:
                    if self.search(word[i + 1:], cur.links[char]):
                        return True
                return False

        return cur.isEnd

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

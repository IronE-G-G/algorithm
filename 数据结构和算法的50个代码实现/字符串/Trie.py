"""
前缀树存储单词
"""


class TreeNode:
    def __init__(self):
        self.links = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.links:
                cur.links[char] = TreeNode()
            cur = cur.links[char]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.links:
                return False
            cur = cur.links[char]
        return cur.isEnd

    def startswith(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.links:
                return False
            cur = cur.links[char]
        return True

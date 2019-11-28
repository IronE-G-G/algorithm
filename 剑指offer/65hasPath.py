# -*- coding:utf-8 -*-
"""
矩阵中的路径：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

思路：遍历找到path的第一个元素，进入判断模式。
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.path = path
        self.length = rows * cols
        for ind, item in enumerate(matrix):
            if item == path[0] and self.judge(ind, path[1:], [ind]):
                return True
        return False

    def judge(self, ind, path, flagSet):
        if not path:
            return True
        # left
        left = ind - 1
        right = ind + 1
        up = ind - self.cols
        down = ind + self.cols
        # 如果上下左右中有元素满足条件（等于path的头个元素并且坑位没被占），递归进入该元素judge下一个
        for item in [left, right, up, down]:
            if 0 <= item < self.length and item not in flagSet and self.matrix[item] == path[0]:
                res = self.judge(item, path[1:], flagSet + [item])
                if res:
                    return True
        return False

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.nrow = len(board)
        if self.nrow == 0:
            return []
        self.ncol = len(board[0])
        self.board = board
        for i in range(0, self.nrow):
            self.dfs(i, 0)
            self.dfs(i, self.ncol - 1)
        for j in range(1, self.ncol - 1):
            self.dfs(0, j)
            self.dfs(self.nrow - 1, j)
        for i in range(0, self.nrow):
            for j in range(0, self.ncol):
                if self.board[i][j] == '*':
                    self.board[i][j] = 'O'
                elif self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
        return self.board

    def dfs(self, i, j):
        if i not in range(0, self.nrow) or j not in range(0, self.ncol) or self.board[i][j] != 'O':
            return
        self.board[i][j] = '*'
        self.dfs(i - 1, j)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i, j + 1)


if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'], ['X', 'O' ,'O', 'X'], ['X', 'X' ,'O' ,'X'], ['X', 'O' ,'X' ,'X']]
    res = Solution().solve(board)
    print(res)

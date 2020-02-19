class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        找到所有跟边界相连的O，标记它。把其他的都置为X，把标记变为O

        对于边界上的元素dfs
        元素不满足条件：return
        如果元素满足条件，置为‘W’，对周围的元素dfs

        把为‘O’的元素都换成‘X’，把为W的换成O

        """

        def dfs(board, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = 'W'
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j - 1)
            dfs(board, i, j + 1)

        if not board:
            return board
        nrow, ncol = len(board), len(board[0])

        # 边界元素执行dfs
        for i in range(nrow):
            dfs(board, i, 0)
            dfs(board, i, ncol - 1)
        for j in range(1, ncol - 1):
            dfs(board, 0, j)
            dfs(board, nrow - 1, j)

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'W':
                    board[i][j] = 'O'
        return board
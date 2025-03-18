class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        lives = []
        deads = []
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for i in range(m):
            for j in range(n):
                num_live_neighbors = 0
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy    
                    if 0<=x<m and 0<=y<n:
                        if board[x][y] == 1:
                            num_live_neighbors += 1
                if num_live_neighbors < 2 and board[i][j] == 1:
                    deads.append((i, j))
                elif board[i][j] == 1 and num_live_neighbors > 3:
                    deads.append((i, j))
                elif board[i][j] == 0 and num_live_neighbors == 3:
                    lives.append((i, j))

        for x, y in deads:
            board[x][y] = 0
        for x, y in lives:
            board[x][y] = 1
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = [(0, 0)]
        visited = [False] * (n**2)
        while queue:
            cur_label, step = queue.pop(0)
            if cur_label == n**2 - 1:
                return step
            for die in range(1, 7):
                next_label = cur_label + die
                if next_label > n**2-1:
                    continue
                row = n - 1 - (next_label // n)
                col = next_label % n if (n-1-row) % 2 == 0 else n - 1 - (next_label % n)
                if board[row][col] != -1:
                    next_label = board[row][col] - 1
                if not visited[next_label]:
                    visited[next_label] = True
                    queue.append((next_label, step+1))
                
        return -1
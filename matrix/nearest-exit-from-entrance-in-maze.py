class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = [(*entrance, 0)]
        while queue:
            x, y, level = queue.pop(0)
            maze[x][y] = "+"
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if maze[nx][ny] == ".":
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return level + 1
                    queue.append((nx, ny, level+1))
        return -1
            
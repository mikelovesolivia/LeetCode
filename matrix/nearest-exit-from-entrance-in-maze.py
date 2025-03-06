class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = collections.deque([(*entrance, 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            x, y, level = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0<= nx < m and 0 <= ny < n and maze[nx][ny] == ".":
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return level + 1
                    queue.append((nx, ny, level+1))
                    maze[nx][ny] = "+"
        return -1
            
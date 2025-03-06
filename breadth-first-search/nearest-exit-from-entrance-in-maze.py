class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        if all(val == "+" for val in maze[0]+maze[-1]) and all(maze[i][0] == "+" and maze[i][-1] == "+" for i in range(m)):
            return -1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = [(*entrance, 0)]
        visited = [[False] * n for _ in range(m)]
        while queue:
            x, y, level = queue.pop(0)
            visited[x][y] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if maze[nx][ny] == ".":
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return level + 1
                    queue.append((nx, ny, level+1))
        return -1
            
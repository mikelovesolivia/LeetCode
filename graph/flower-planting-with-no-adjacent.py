class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i, j in paths:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        visited = [0] * n
        colors = [0] * n
        colors[0] = 0
        def bfs(node_selected):
            queue = [node_selected]
            while queue:
                node = queue.pop(0)
                visited[node] = 1
                color_used = [0] * 4
                for neighbor in graph[node]:
                    if visited[neighbor]:
                        nbr_color = colors[neighbor]
                        color_used[nbr_color] = 1
                for c, used in enumerate(color_used):
                    if not used:
                        color = c 
                        break
                colors[node] = color
                visited[node] = 1
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        for node in range(n):
            if not visited[node]:
                bfs(node)
        return [x + 1 for x in colors]
                

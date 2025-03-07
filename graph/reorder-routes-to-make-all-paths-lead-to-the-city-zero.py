class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        directed_graph = [set() for _ in range(n)]
        for u, v in connections:
            graph[u].add((v, 1))
            graph[v].add((u, -1))
        visited = [False] * n
        
        def dfs(node):
            if visited[node]:
                return 0
            count = 0
            visited[node] = True
            for neighbor, direction in graph[node]:
                if not visited[neighbor] and direction == 1:
                    count += 1
                count += dfs(neighbor)
            return count
        return dfs(0)
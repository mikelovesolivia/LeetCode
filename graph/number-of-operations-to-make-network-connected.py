class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        graph = [set() for _ in range(n)]
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)
        visited = [0] * n
        def dfs(i):
            if visited[i]:
                return
            visited[i] = 1
            for j in graph[i]:
                dfs(j)
            return
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count - 1 
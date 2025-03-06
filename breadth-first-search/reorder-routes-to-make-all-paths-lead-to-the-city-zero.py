class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        for u, v in connections:
            graph[u].add(v)
        return graph
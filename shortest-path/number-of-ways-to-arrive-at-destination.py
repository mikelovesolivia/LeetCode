class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        paths = [0] * n
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        distances = {node: float('inf') for node in graph}
        distances[0] = 0
        paths[0] = 1
        pq = [(0, 0)]
        while pq:
            cur_d, cur_node = heapq.heappop(pq)
            if cur_d > distances[cur_node]:
                continue
            for neighbor, weight in graph[cur_node]:
                d = cur_d + weight
                if d < distances[neighbor]:
                    distances[neighbor] = d
                    heapq.heappush(pq, (d, neighbor))
                    paths[neighbor] = paths[cur_node]
                elif d == distances[neighbor]:
                    paths[neighbor] += paths[cur_node]
        return paths[n-1]
        
        return res
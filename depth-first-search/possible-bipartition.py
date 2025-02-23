class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for i, j in dislikes:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        color = [-1] * n

        for i in range(n):
            if color[i] != -1:
                continue
            queue = [i]
            color[i] = 0
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    else:
                        if color[neighbor] == color[node]:
                            return False
        return True

        
        
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
      
        ans = 0
        for i in range(n):
            for j in range(m):
                if i > 0 and matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
            cur_row = sorted(matrix[i], reverse=True)
            for j in range(m):
                ans = max(ans, cur_row[j] * (j+1))
            return ans    
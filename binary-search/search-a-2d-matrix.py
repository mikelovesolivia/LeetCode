class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m*n-1
        while left<=right:
            mid = (left+right)//2
            row_mid = mid // n
            col_mid = mid % n
            if matrix[row_mid][col_mid] == target:
                return True
            elif matrix[row_mid][col_mid] > target:
                right = mid - 1
            elif matrix[row_mid][col_mid] < target:
                left = mid + 1
        return False
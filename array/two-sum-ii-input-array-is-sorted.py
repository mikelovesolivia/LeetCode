class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        while left<right:
            twosum = numbers[left] + numbers[right]
            if twosum == target:
                return [left+1, right+1]
            elif twosum > target:
                right -= 1
            else:
                left += 1
        return
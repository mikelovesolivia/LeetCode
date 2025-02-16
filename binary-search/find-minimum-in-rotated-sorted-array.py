class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = nums[0]
        n = len(nums)
        if n == 1:
            return pivot
        elif n==2:
            return min(nums)
        left = 1
        right = n-1
        if nums[left]<nums[right]:
            return min(pivot, nums[left])
        while left<=right:
            mid = (left+right)//2
            if nums[left]<pivot:
                return nums[left]
            
            elif left!=right:
                if nums[mid]>pivot:
                    left = mid+1
                if nums[mid]<pivot:
                    right=mid
            else:
                return nums[left]

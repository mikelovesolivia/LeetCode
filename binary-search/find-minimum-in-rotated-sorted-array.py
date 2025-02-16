class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = nums[0]
        n = len(nums)
        if n == 1:
            return pivot
        left = 1
        right = n-1
        if nums[left]<nums[right]:
            return pivot
        while left<=right:
            mid = (left+right)//2
            if nums[left]<pivot:
                return nums[left]
            elif nums[right]>pivot:
                return nums[right]
            elif left!=right:
                if nums[mid]>pivot:
                    left = mid+1
                if nums[mid]<pivot:
                    right=mid-1
            else:
                return nums[left]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            left = i+1
            right = n-1
            while left<right:
                twosum = nums[left] + nums[right] 
                if twosum == target:
                    ans.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right>left and nums[right] == nums[right+1]:
                        right -= 1
                elif twosum < target:
                    left += 1
                else:
                    right -= 1
        return ans
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-2):
            target = - nums[i]
            left = i+1
            right = n-1
            while left<right:
                twosum = nums[left] + nums[right] 
                if twosum == target:
                    ans.add(tuple(sorted([-target, nums[left], nums[right]])))
                    left += 1
                    right -= 1
                elif twosum < target:
                    left += 1
                else:
                    right -= 1
        return list(ans)
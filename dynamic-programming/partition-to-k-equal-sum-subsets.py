class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        SUM = sum(nums)
        if SUM % k != 0:
            return False
        target = SUM // k

        subsum = [0] * k
        nums.sort(reverse=True)
        def backtrack(i):
            if i == len(nums):
                for j in range(k):
                    if subsum[j] != target:
                        return False
                return True

            for j in range(k):
                if subsum[j] + nums[i] <= target:
                    subsum[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    subsum[j] -= nums[i]
            return False
        return backtrack(0)
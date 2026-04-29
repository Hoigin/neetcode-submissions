from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums) // 2
        residual = sum(nums) % 2
        if residual != 0:
            return False
        @cache
        def backtrack(start, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target:
                return False
            for i in range(start+1, n):
                curr_sum += nums[i]
                if backtrack(i, curr_sum):
                    return True
                curr_sum -= nums[i]
            return False
        return backtrack(0, 0)
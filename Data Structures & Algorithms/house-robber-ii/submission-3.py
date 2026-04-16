class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        nums1 = nums[:-1]
        nums2 = nums[1:]
        dp1 = [-1] * (length-1)
        dp2 = [-1] * (length-1)
        def dfs(dp, nums, i):
            if i >= length-1:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i]+dfs(dp, nums, i+2), dfs(dp, nums, i+1))
            return dp[i]
        return max(dfs(dp1, nums1, 0), dfs(dp2, nums2, 0))
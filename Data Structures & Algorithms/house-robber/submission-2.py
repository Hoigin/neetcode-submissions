class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [-1] * length
        def dfs(i):
            if i >= length:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return dp[i]
        return dfs(0)
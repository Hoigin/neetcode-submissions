class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-math.inf]*n for i in range(n)]
        res = -math.inf
        for end in range(n):
            for start in range(end, -1, -1):
                if start == end:
                    dp[start][end] = nums[start]
                else:
                    dp[start][end] = dp[start+1][end]*nums[start]
                res = max(res, dp[start][end])
        return res
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n==0 or n==1:
            return 0
        dfs = [0]*(n+1)
        for i in range(2, n+1):
            dfs[i] = min(dfs[i-1]+cost[i-1], dfs[i-2]+cost[i-2])
        return dfs[n]
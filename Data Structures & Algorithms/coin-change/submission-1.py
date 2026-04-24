class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. 初始化 dp 数组，长度为 amount + 1
        # 初始值设为 amount + 1（比凑成该金额所需的最大硬币数还大，相当于正无穷）
        dp = [amount + 1] * (amount + 1)
        
        # 2. 基础情况：凑齐金额 0 需要 0 枚硬币
        dp[0] = 0
        
        # 3. 遍历从 1 到 amount 的所有金额
        for i in range(1, amount + 1):
            # 对于每个金额，尝试每一种硬币
            for coin in coins:
                # 如果当前金额大于或等于硬币面值，说明可以尝试放入这枚硬币
                if i - coin >= 0:
                    # 状态转移方程：
                    # 当前金额的最优解 = min(当前记录的解, 减去一个硬币面值后的金额的最优解 + 1)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 4. 如果 dp[amount] 仍为初始值，说明无法凑齐，返回 -1
        return dp[amount] if dp[amount] != amount + 1 else -1
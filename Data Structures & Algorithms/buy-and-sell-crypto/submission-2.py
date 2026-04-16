class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        n = len(prices)
        while right < n:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
                right += 1
            else:
                left = right
                right += 1
        return max_profit
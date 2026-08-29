class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_price = [prices[n-1]] * n
        min_price = [prices[0]] * n

        for i in range(1, n):
            max_price[n-i-1] = max(prices[n-i-1], max_price[n-i-2])
            min_price[i] = min(prices[i], min_price[i-1])

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_price[i] - min_price[i])

        return max_profit
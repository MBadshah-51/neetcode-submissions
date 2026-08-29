class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        l = 0 
        r = 1

        max_profit = 0

        while r < n:
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r
            r += 1

        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, min_price = -1, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            res = max(res, profit)

        return res
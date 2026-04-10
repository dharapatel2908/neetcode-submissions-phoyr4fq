class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minbuy = prices[0]

        for sell in prices:
            maxprofit = max(maxprofit, sell- minbuy)
            minbuy = min(sell, minbuy)
        return maxprofit
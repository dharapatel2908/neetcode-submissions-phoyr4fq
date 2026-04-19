class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                sell = prices[right]- prices[left]
                maxprofit = max(maxprofit, sell)
            else:
                left = right
            right+=1
            
        return maxprofit
        
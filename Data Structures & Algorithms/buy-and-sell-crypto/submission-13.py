class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        Max = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                Max = max(curr, Max)
            else:
                l = r
            r += 1
        
        return Max
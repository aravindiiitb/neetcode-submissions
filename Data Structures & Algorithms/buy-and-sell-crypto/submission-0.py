class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRight = [prices[-1]]
        for i in range(len(prices)-1, 0, -1):
            maxRight.insert(0, max(maxRight[0], prices[i]))
                
        res = 0
        for i in range(len(prices)):
            if prices[i] <= maxRight[i]:
                res = max (maxRight[i] - prices[i], res)
        
        return res

        
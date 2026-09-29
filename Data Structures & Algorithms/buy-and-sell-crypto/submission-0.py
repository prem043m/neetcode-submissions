class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = prices[0]

        for i in range(len(prices)):
            currprofit = prices[i]-minprice
            maxprofit = max(maxprofit,currprofit)
            minprice = min(minprice,prices[i])
        return maxprofit
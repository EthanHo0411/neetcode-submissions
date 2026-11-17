class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #since the sell date is always ahead of the buying day , slide windows can be used
        #move the left side of the window whenver theres a cheaper price
        #the selling cnt happen before the cheaper price anyway

        maxprofit = 0
        i = 0 
        for j in range(1, len(prices)):
            profit = prices[j] - prices[i]
            maxprofit = max(maxprofit, profit)

            if prices[j] < prices[i]:
                i = j 
        return maxprofit

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        mini = 10000000
        maxi = 0
        for i in range(n):
            # getting the minimum of prices
            if prices[i] < mini:
                mini = prices[i]
            # maximum values is the differnece between current price to minimum value and the current maximum value
            elif prices[i]-mini > maxi:
                maxi = prices[i] - mini
        return maxi

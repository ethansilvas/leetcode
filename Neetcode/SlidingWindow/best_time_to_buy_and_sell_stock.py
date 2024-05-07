"""
loop through the stocks keeping track of the mininum price
each time you will calculate the maximum between the current highest profit
and the profit between the current price and the lowest price
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        min_price = prices[0]

        for price in prices: 
            if price < min_price:
                min_price = price
            
            profit = max(profit, price - min_price)

        return profit
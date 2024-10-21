# Leetcode 121
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        min_cost = prices[0]
        for price in prices:
            prof = price-min_cost
            if price < min_cost:
                min_cost = price
            res = max(res, prof)
        return res

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        max_val = sum(prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i-1] < prices[i])
        return max_val

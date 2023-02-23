class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        v1, v2 = 0,0

        for i in range(1, len(prices)):
            temp = v1
            v1 = max(v1 + prices[i] - prices[i-1], v2)
            v2 = max(temp, v2)
        return max(v1, v2)
class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        
        dp = [0] * len(values)
        dp[0] = values[0]
        max_value = 0

        for i in range(1, len(values)):
            dp[i] = max(dp[i-1], values[i-1] + i - 1 )
            max_value = max(max_value, dp[i] + values[i] - i)

        return max_value
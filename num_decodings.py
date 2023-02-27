class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 :
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1


        for i in range(2,n+1):
            if 10 <= int(s[i-2:i]) <= 26 :
                dp[i] += dp[i-2]
            if 0 < int(s[i-1:i]) <= 9 : 
                dp[i] += dp[i-1]

        return dp[-1]





# bu yöntem daha hızlı 
#
# class Solution(object):
#     def numDecodings(self, s):
# 		if not s:
# 			return 0
# 		dp = [0] * (len(s) + 1)
# 		dp[0] = 1
# 		dp[1] = 1 if s[0] != '0' else 0
# 		for i in range(2, len(s) + 1):
# 			if s[i - 1] != '0':
# 				dp[i] += dp[i - 1]
# 			if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
# 				dp[i] += dp[i - 2]
# 		return dp[-1]
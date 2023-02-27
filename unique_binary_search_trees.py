class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp =[0] * ( n + 1 ) # 0 array' i oluşturuluyor
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1): # mevcut noktaya kadar olan değerlere ait alt ağaçların hesaplanması için kullanılan ikinci değişken
                dp[i] += dp[j-1] * dp[i-j] # alt agaclara ait butun kombinasyonlar hesaplanıyor
        
        return dp[-1]
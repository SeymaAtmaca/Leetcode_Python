class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # bu çözüm, leetcode kullanıcılarından coderMann e aittir. 
        # Çözüme ait açıklama sayfası :  https://leetcode.com/problems/coin-change/solutions/3246644/best-solution-explained-with-illustrations/
        minCoins = [float('inf') for i in range(amount + 1 )]

        minCoins[0] = 0

        for i in range(1, amount+1):
            for coin in coins: 
                if i - coin >= 0:
                    minCoins[i] = min(minCoins[i], 1+minCoins[i - coin])
        
        return minCoins[amount] if minCoins[amount] != float('inf') else -1
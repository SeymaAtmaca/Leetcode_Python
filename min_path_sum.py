class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)] # grid boyutunda dp olusturuluyor
        dp[0][0] = grid[0][0] # baslangic noktasi

        for i in range(1, m): # ilk sutun toplam maliyeti hesabi
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, n):   # ilk satir toplam maliyeti hesabi
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):   # ilk satir ve sutunlar hesaplandigi icin range 1 den sonrası icin aliniyor
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) # mevcut hucre ile minimum degere sahip hucrenin maliyeti toplami dp ye yaziliyor

        return dp[-1][-1]
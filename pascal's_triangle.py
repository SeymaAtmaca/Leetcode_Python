class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = []

        for i in range(1, numRows + 1):
            row = [1] * i          # her döngüde farklı satır sayısı yer aldığı için tekrarlı oluşturma yapıldı
            for j in range(1, i-1):
                row[j] = dp[i-2][j] + dp[i-2][j-1]
            dp.append(row)

        return dp
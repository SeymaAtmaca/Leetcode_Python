
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_len, w2_len = len(word1),  len(word2)
        @lru_cache(None) # bellek kullanımı ve hız açısından lru_cache çok önemli. Yaklaşık 5-6 kat iyileştirme sağlıyor.

        def dp(i, j):
            if i >= w1_len : return w2_len -j 
            if j >= w2_len : return w1_len - i
            if word1[i] == word2[j]: return dp(i+1, j+1) 

            return min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1)) + 1

        return dp(0,0)


# bu çözüm yaklaşık % 60 daha hızlıdır

        # @lru_cache(None)
        # def dp(i, j):
        #     if i == 0: return j  # Need to insert j chars
        #     if j == 0: return i  # Need to delete i chars
        #     if s1[i-1] == s2[j-1]:
        #         return dp(i-1, j-1)
        #     return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
        
        # return dp(len(s1), len(s2))
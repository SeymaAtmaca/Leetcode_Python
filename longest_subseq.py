class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #belleğin temizlenmesi ve çalışma zamanının arttırılması için çok önemli 
        @cache  
        def f(s):
            if not s:
                return 0
            ans = 1
            for c in string.ascii_lowercase: # ascii karakterler tek tek alınır
                i, j = s.find(c), s.rfind(c) # konumları bulunur. burada find(), harfin bulunduğu ilk konumu döndürür
                #print("i: ", i, "j : ", j, "c : ", c)
                if i != j:  # eğer ilk konum ve sonraki konumlar eşitse, yani bu harften tek bir tane  varsa dikkate alınmaz. Farklıysa alt arama işlemi yapılır.
                    ans = max(ans, f(s[i+1:j]) + 2)
            return ans
        return f(s)
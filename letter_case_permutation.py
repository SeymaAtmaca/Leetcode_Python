class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]

        for i in range(len(s)):
            if s[i].isnumeric(): # eger gelen sonraki deger sayı ise ;
                for p in range(len(result)):    # result icindeki her deger icin bir dongu kur
                    result[p] = result[p] + (s[i])  # sayıyı result icindeki her degere ekle
        
            if s[i].isalpha():  # eger gelen harf ise
                result = result * 2 # permutasyon olusturabilmek icin result' u iki ile carp 
                                # result = "1" ve gelen deger "a" ise burada result = "1a", "1A" yapılmalı bu nedenle iki tane 1 e ihtiyac var. 
                for p in range(len(result)):    # result taki her degere erismek icin bir dongu kur
                    if (p*2 < len(result)):
                        result[p] = result[p] + (s[i].lower())  # yarısına kucuk harf olarak
                    else:
                        result[p] = result[p] + (s[i].upper())  # yarısına buyuk harf olarak ekle
                
        return result   # permutasyonları iceren result u return et

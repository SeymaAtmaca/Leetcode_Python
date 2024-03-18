class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) : return false
        for i in range(len(s)):
            if(s.find(s[i], i+1) != t.find(t[i], i+1)):
                return False
        
        return True

# daha hızlı bir yöntem ise şu :
# return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
# burada string lerin karşılıklı elemanları zip ile eşleştirilir ve set edilir,
# aynı zamanda s ve t de set içine alınır.
# en son oluşturulan üç set in uzunluğuna bakılır
# eğer uzunluklar eşitse bu iki değer isomorphic tir denir.
# çünkü bir string in karakterinin karşı tarafta karşılığı yoksa burada length uzunluğu daha fazla olur.        
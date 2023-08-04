class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        
        n = len(derived)
        arr = [0] * n
        for i in range(n-1):
            arr[i+1] = arr[i] ^ derived[i]

        for i in range(n):
            if derived[i] != arr[i]^arr[(i+1) % n] : return False
        return True



# bu çözüm hem daha hızlı hem de bellek kullanımı açısından daha efektif. 
# Leetcode da sunulmuş en iyi çözümlerden
# class Solution(object):
#     def doesValidArrayExist(self, derived):
#         """
#         :type derived: List[int]
#         :rtype: bool
#         """
#         def _try(fst,derived):
#             last=fst
#             for d in derived[:-1]:last=1-last if d==1 else last
#             return (derived[-1] and fst!=last) or (not derived[-1] and fst==last)

#         return _try(1,derived) 
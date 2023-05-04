class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        all_pro = [] # butun olasiliklar burada toplaniyor

        def generate(left, right, cache):
            if len(cache) == n * 2:
                all_pro.append(cache)   # alt cagirimlarin her biri bu noktada tek tek sonlanacak. 
                                        # Butun recursive cagirimlar bittiginde ana return e gidilecek.
                return 
            
            if left < n :
                generate(left + 1 , right, cache + '(')
            if right < left :   # parantezlerin dogru eslesmesi icin burasi right < left seklinde kontrol edilmeli
                generate(left, right + 1, cache + ')')
            
        generate(0,0,'')
        return all_pro




# bu cozum daha hizli
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []
#         def helper(openN, closedN):
#             if openN==closedN==n:
#                 res.append(''.join(stack))
#                 return
            
#             if openN<n:
#                 stack.append('(')
#                 helper(openN+1,closedN)
#                 stack.pop()
#             if closedN<openN:
#                 stack.append(')')
#                 helper(openN, closedN+1)
#                 stack.pop()
#         helper(0,0)
#         return res
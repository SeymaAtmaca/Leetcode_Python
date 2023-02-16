class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1 or n == 2 :
            return 1
        if n == 0:
            return 0
        else : 
            return Solution.tribonacci(self, n-1) + Solution.tribonacci(self, n-2) + Solution.tribonacci(self, n-3)
        
solution = Solution()
print("Result : ", solution.tribonacci(30))
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return n
        else : 
            return Solution.fib(self, n-1) + Solution.fib(self, n-2)


solution = Solution()
print("Result : ", solution.fib(5))
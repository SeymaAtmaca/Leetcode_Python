"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val = num
        check = []
        if n == 1 : return True
        while(True):
            digits = list(map(int, str(val)))
            top = 0
            for i in digits: top += pow(i,2)
            if top == 1 : return True
            if top in check: return False
            check.append(top)
            val = top

        

solution = Solution()
num = 7
result = solution.isHappy(num)
print(result)
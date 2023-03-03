class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        fac_m, fac_n, fac_all = 1, 1, 1

        if m-1 >= n-1 :
            i = 1
            while i <= n-1 : 
                fac_n = i * fac_n
                i += 1
            
            i = m 
            while i <= ( m+n-2):
                fac_all *= i
                i += 1

            return fac_all / fac_n

        if n-1 > m-1 :
            i = 1
            while i <= m-1 : 
                fac_m = i * fac_m
                i += 1
            
            i = n 
            while i <= ( m+n-2):
                fac_all *= i
                i += 1

            return fac_all / fac_m
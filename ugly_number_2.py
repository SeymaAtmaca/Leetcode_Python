class Solution(object):
    def nthUglyNumber(self, k):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * k
        i2 = i3 = i5 = 0
        res[0] = 1
        for i in range(1, k):
            res[i] = min(res[i2]*2 , res[i3] * 3 , res[i5] * 5 )
            if res[i] == res[i2] * 2 : i2 += 1
            if res[i] == res[i3] * 3 : i3 += 1
            if res[i] == res[i5] * 5 : i5 += 1
        return res[-1]
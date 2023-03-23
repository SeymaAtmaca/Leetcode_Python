# 80% beats for this solution
# her bir değer için xor işlemi yapılır. Tüm dizi için for dongusu bittiğinde result içinde, tekrar etmeyen değer bulunur.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        
        return result
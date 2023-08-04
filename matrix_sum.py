import numpy as np
class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        for col in nums : col.sort()
        return np.sum(np.max(np.array(nums), axis=0))
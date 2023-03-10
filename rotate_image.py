import numpy as np
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        new = np.array(matrix)
        for i in range(len(matrix)):
            new[:,i] = matrix[::-1][i] 
        matrix[:] = new[:]
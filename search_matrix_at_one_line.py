class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    
        return any(matrix[i][j] == target for i in range(len(matrix)) for j in range(len(matrix[0])))

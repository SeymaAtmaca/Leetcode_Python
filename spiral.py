class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """


        result = []
        while matrix:
            result += matrix.pop(0) 

            if matrix and matrix[0]:  
                for line in matrix:
                    result.append(line.pop())

            if matrix: 
                result += matrix.pop()[::-1]

            if matrix and matrix[0]: 
                for line in matrix[::-1]:
                    result.append(line.pop(0))
        return result
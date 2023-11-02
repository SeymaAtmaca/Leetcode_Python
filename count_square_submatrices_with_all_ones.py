class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])

        @cache
        def dp(i,j):
            if matrix[i][j] == 1 : 
                if i != 0 and j != 0 : 
                   return min(dp(i-1,j), dp(i, j-1), dp(i-1,j-1)) + 1 
                else : return 1
            else : 
                return 0

        return sum(dp(i,j) for i in range(m) for j in range(n)) 
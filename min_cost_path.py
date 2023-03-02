class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:


        for i in reversed(range(len(matrix) - 1)):  # sutun
            for j in range(len(matrix[0])): # satir
                right = inf if j == len(matrix) - 1 else matrix[i+1][j+1]
                left = inf if j == 0 else matrix[i+1][j-1]
                down = matrix[i+1][j]

                matrix[i][j] += min(right, left, down)

        return min(matrix[0])
    

# aşağıdaki yöntem daha hızlı. Burada uzunluk sonuçlarını dizinin son elemanına toplayacak şekilde bir
# işlem yapılıyor. BU nedenle return için matrix[-1] kullanılıyor

# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         for i in range(1,len(matrix)):
#             for j in range(1,len(matrix[0])-1):
#                 matrix[i][j] = matrix[i][j] + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
            
#             matrix[i][0] = matrix[i][0] + min(matrix[i-1][0], matrix[i-1][1])
#             matrix[i][-1] = matrix[i][-1] + min(matrix[i-1][-2], matrix[i-1][-1])
            
#         return min(matrix[-1])
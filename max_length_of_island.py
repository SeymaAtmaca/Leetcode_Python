class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def calculate(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0:
                return 0 
            grid[i][j] = 0
            return 1 + calculate(i+1, j) + calculate(i-1, j) + calculate(i, j+1) + calculate(i, j-1)


        m, n = len(grid), len(grid[0])
        max_length_of_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_length_of_island = max(max_length_of_island, calculate(i,j))

        return max_length_of_island
            
## aşağıdaki yöntem daha hızlı 
# class Solution(object):
#     def maxAreaOfIsland(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """ 
#         res = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     res = max(res, self.area(grid, i, j))
#         return res

#     def area(self,grid, i, j):
#         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])  or grid[i][j] != 1:
#             return  0
#         grid[i][j] = "#"
#         return 1 + self.area(grid, i - 1, j) + self.area(grid, i + 1, j) + self.area(grid, i, j - 1) + self.area(grid, i, j + 1)
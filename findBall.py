class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        ans = []

        for c in range(m):
            x = c
            for r in range(n):
                slope = grid[r][x]
                x += slope
                if x < 0 or x >= n or grid[r][x] != slope:
                    ans.append(-1)
                    break
            else:
                ans.append(x)


solution = Solution()
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
result = solution.findBall(grid)
print(result)
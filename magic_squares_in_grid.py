class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt = 0
        direct = [[(-1,0), (0,0), (1,0)], [(-1,-1), (0,-1), (1,-1)], [(-1,1), (0,1), (1,1)], [(0,-1), (0,0), (0,1)], [(-1,-1), (-1,0), (-1,1)], [(1,-1), (1,0), (1,1)], [(-1,-1), (0,0), (1,1)], [(1,-1), (0,0), (-1,1)]]

        for i, j in product(range(1, len(grid)-1), range(1, len(grid[0])-1)):
            if all(grid[i+x1][j+x2]+grid[i+y1][j+y2]+grid[i+z1][j+z2] == 15 for (x1,x2), (y1,y2), (z1, z2) in direct) and sum(1 << i for i in chain(grid[i-1][j-1:j+2], grid[i][j-1:j+2], grid[i+1][j-1:j+2])) == 1022:
                cnt += 1
        return cnt 
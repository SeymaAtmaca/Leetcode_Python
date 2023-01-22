# problem aşağıda verilmiştir.
# 2 ile gösterilen konumda çürük portakallar bulunmaktadır.
# her dakika, çürük portakalların alt-üst ve iki yanında bulunan taze portakallar( 1 ) çürümektedir.
# büm taze portakalların çürümesi için gereken süre kaç dakikadır ? 


# örnekte verilen matris aşağıdadır.
# [çürük, taze, taze]
# [taze, taze, boş]
# [boş, taze, taze]

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        r = len(grid)
        c = len(grid[0])

        rotting = {(i,j) for i in range(r) for j in range(c) if grid[i][j] == 2}
        fresh = {(i,j) for i in range(r) for j in range(c) if grid[i][j] == 1}
        timer = 0

        while fresh:
            if not rotting: return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0,1),(1,0),(0,-1),(-1,0)] if grid[di][dj]}
            fresh -= rotting
            timer += 1

        return timer


solution =Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
result = solution.orangesRotting(grid)
print(result)
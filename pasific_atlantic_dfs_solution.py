 
"""
Kısaca soru ; 
Pasifik ve Atlantik okyanuslarına kıyısı olan bir matris adası veriliyor. Matriste bulunan her hücredeki değer, o hücrenin deniz yüzeyine göre
yüksekliğini vermektedir. Yağmur yağdığı düşünülürse, hangi noktalara biriken su, pasifik ve atlantik sularını birleştirir. Burada birleştirmeden maksat şu şekilde;
odaklanılan hücreye yağmur suyu dolduktan sonra üst-alt-sağ-sol hücrelerin değeri, eğer odaklanılan hücrenin değerinden ( denize göre yüksekliği) küçükse veya eşitse
bu hücrelere yağmur uyu taşıyor. Bu taşan sular ile koşu hücreler doluyor. Bu olay sonucu Pasifik ve Atlantik sularına kadar uzanabilen path' lerin bulunması isteniyor.

Verilen açıklama ; 
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans. 
"""



class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        row_ = len(heights)
        column_ = len(heights[0])

        def dfs(row, column, heights, visited, prev):
            if row < 0 or row >= row_ or column < 0 or column >= column_ or ((row,column) in visited) or heights[row][column] < prev:
                return
            
            visited.add((row,column))
            
            dfs(row + 1, column, heights, visited, heights[row][column])
            dfs(row - 1, column, heights, visited, heights[row][column])
            dfs(row, column + 1, heights, visited, heights[row][column])
            dfs(row, column - 1, heights, visited, heights[row][column])

            
            

        pacific = set()
        atlantic = set()
        for i in range(row_):
            dfs(i, 0, heights, pacific, float('-inf'))
            dfs(i, column_ - 1, heights, atlantic, float('-inf'))
            
        for i in range(column_):
            dfs(0, i, heights, pacific, float('-inf'))
            dfs(row_ - 1, i, heights, atlantic, float('-inf'))
            
        intersectedArr = list(pacific & atlantic)
        print(intersectedArr)
        return intersectedArr

import numpy as np
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
solution = Solution()
solution.pacificAtlantic(heights)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

            n = len(triangle)
            for i in range(n-2, -1, -1):
                for j in range(len(triangle[i])):
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
            return triangle[0][0]

        # n = len(triangle)
        # if n == 0:
        #     return 0
        # if n == 1 : 
        #     return min(triangle[0])
        # c = 0

        # for i in range(n-1):
        #     right = inf if c == len(triangle) - 1 else triangle[i + 1][c + 1]
        #     left = inf if c == 0 else triangle[i+1][c-1]
        #     down = triangle[i+1][c]
        #     min_val = min(right, left, down)
        #     if min_val == right:
        #         c += 1
        #     elif min_val ==  left :
        #         c -= 1
        #     triangle[0][0] += min_val

        # return triangle[0][0]


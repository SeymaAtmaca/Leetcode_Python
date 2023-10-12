class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        ret = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                count = 0
                for di, dj in [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and board[ni][nj] == 1:
                        count += 1

                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        ret[i][j] = 0
                    else:
                        ret[i][j] = 1
                elif board[i][j] == 0 and count == 3:
                    ret[i][j] = 1

        for i in range(r):
            for j in range(c):
                board[i][j] = ret[i][j]

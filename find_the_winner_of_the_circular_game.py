class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        last_winner = 0
        circle = [i for i in range(1,n+1)]
        while len(circle) != 1 :
            pointer = (last_winner + k - 1 ) % len(circle) # loser position 
            circle.remove(circle[pointer])
            last_winner = pointer 
        return int(circle[0])
        
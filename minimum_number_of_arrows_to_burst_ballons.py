class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])

        cnt = 1
        end = points[0][1] 

        for i in range(1, len(points)):
            start, curr_end = points[i]
            if start > end:
                cnt += 1
                end = curr_end 
        return cnt

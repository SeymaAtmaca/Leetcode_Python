class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area, l, r = 0, 0, len(height) - 1 
        while l < r :
            area = (r - l) * min(height[l] , height[r])
            max_area = max(area, max_area)
            if height[l] < height[r] : l += 1
            else : r -= 1
        return max_area
        
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(list(map(lambda x: pow(x,2), nums)))

solution = Solution()
nums = [-1,2,3,-4]
result = solution.sortedSquares(nums)
print(result)
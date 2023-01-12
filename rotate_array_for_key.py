class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] =  nums[-k:] + nums[:-k]


solution = Solution()
nums = [1,2,3,4,5,6,7]
result = solution.rotate(nums, 3)
print(result)
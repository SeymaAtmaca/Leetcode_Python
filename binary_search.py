class Solution(object):
    def search(self, nums, target):
        min = 0
        max = len(nums) - 1 
        while min <= max:
            mean = int((max + min) / 2 ) 
            if target == nums[mean] :
                return mean

            elif nums[mean] < target:
                min = mean + 1

            else :
                max = mean - 1
        return -1

solution = Solution()
nums = [-1,0,3,5,9,12,15]
result = solution.search(nums, -1)
print(result)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        for i in range(len(nums)):
            while (i-1) >= 0 and nums[i] == nums[i-1] and nums[i] != '_':
                count -= 1
                nums.remove(nums[i-1])
                nums.append('_')
        return count


        #================== Python set lerde birden fazla aynı eleman bulunamaz ! 
        # nums[:] = sorted(set(nums))
        # return len(nums)


        #========= 
        # distinct = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[distinct] = nums[i]
        #         distinct += 1
        # return distinct


solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
result = solution.removeDuplicates(nums)
print(nums, " result  : ", result)
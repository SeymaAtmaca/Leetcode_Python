class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1 :
            return 0

        step, current, max_reach = 0, 0 , 0 

        for i in range( len(nums)):
            if i > current: 
                step += 1
                current = max_reach
            max_reach = max(max_reach, i + nums[i])

        return step 
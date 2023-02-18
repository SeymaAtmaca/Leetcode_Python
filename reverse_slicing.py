class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            
            if x <= i + nums[i]:x = i
            print(" i : ", i, " nums[i] : ", nums[i], " x: ", x)
        return x==0
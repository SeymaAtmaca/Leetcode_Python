class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def calculate(p):
            last,now = 0,0
            for i in p: last,now = now, max(last + i, now)
            return now

        if len(nums) <= 3:
            return max(nums)

        p_1 = nums[1:]
        p_2 = nums[0:-1]

        return max(calculate(p_1), calculate(p_2))
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n, sum_nums = len(nums), sum(nums)
        maks, tmp_maks, mini, tmp_mini = -float('inf'), 0,0, float('inf')

        for i in nums : 
            tmp_maks += i
            maks, tmp_maks = max(maks, tmp_maks), max(0, tmp_maks)

            tmp_mini += i
            mini, tmp_mini = min(mini, tmp_mini), min(0, tmp_mini)

        return max(maks, sum_nums - mini)
        
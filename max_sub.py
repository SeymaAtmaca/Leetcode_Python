class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None :
            return 0
        if len(nums) == 1 :
            return int(nums[0])

        max_sub = nums[0]
        current_sum = 0

        for i in nums:
            if current_sum < 0 :
                current_sum = 0
            current_sum += i
            max_sub = max(max_sub, current_sum)
        return max_sub


## aşağıdaki yöntem daha hızlı ve bellek kulalnımı daha az : 
# def maxSubArray(self, nums):
#         res = nums[0]

#         total = 0
#         for n in nums:
#             total += n
#             res = max(res, total)
#             if total < 0:
#                 total = 0
#         return res
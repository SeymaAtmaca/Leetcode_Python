class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        if not nums: return 0
        def robbing( index):
            if index >= len(nums):    return 0
            if index not in res :
                res[index] = max(robbing(index + 1), nums[index] + robbing(index + 2))
            return res[index]
        return robbing(0)


        # asagidaki kod daha hizli ve daha temiz bir kod !!
        # last, now = 0, 0
        # for i in nums: last, now = now, max(last + i, now)  
        # return now
    
solution = Solution()
nums = [10,20,2,78,98]
result = solution.rob(nums)
print(result)
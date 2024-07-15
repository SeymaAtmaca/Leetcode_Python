class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)-1, -1, -1):
                # ilerleme için gerekn kadar büyük bir sayıya sahip miyim ve olduğum konuma erişebiliyor muyum ( dp[j] )
                if nums[j] >= len(nums-1) and dp[j]:
                    dp[i] = True
                    break
        
        return dp[-1]
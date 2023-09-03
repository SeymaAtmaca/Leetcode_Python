class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        m = s
        for i in range(0, len(nums) - k):
            s = s + nums[i+k] - nums[i]
            m = max(m, s)
        return m / k
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_max_reach, next_max_reach = 0, 0

        for i in range(len(nums)-1):
            next_max_reach = max(next_max_reach, i + nums[i])
            if i == cur_max_reach:
                jumps += 1
                cur_max_reach = next_max_reach
        
        return jumps
        
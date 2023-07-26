class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            if i - k < 0 or i + k + 1 > len(nums):
                continue
            sub_1 = nums[i - k:i]  # alt kume
            sub_2 = nums[i + 1:i + k + 1]  # ust kume
            if all(sub_1[j + 1] <= sub_1[j] for j in range(len(sub_1) - 1)):
                if all(sub_2[j + 1] >= sub_2[j] for j in range(len(sub_2) - 1)):
                    ret.append(i)
            else : continue
        return ret
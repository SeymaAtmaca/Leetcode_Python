class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # eger dizideki tüm sayilar nums[j] < nums[i] < nums[k] yi sağliyorsa 2 dondur
        if all(( nums[j] < nums[i] and nums[k] < nums[i+1]) for i in range(1, len(nums) - 1) for j in range(0, i) for k in range(i, len(nums) -1 )) :return 2
        # ard arda olan sayilarin bazilari asagidaki kontrolu sagliyorsa 1 dondur
        if any(( nums[i - 1 ] < nums[i] and nums[i] < nums[i+1]) for i in range(1, len(nums) - 1)) :return 1
        # sonuc alinamadiysa 0 dondur
        return 0
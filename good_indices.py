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


        
# ayni soru cin uretilen yukaridaki cozum dogru olmakla beraber, uretilen diger cozumlere gore bir miktar yavas kalmaktadir.
        # asagida verilen coum mantigi, uretilen cozume biraz daha yakin olmakla beraber daha hizli bir yontemdir. 
        
        # ret = []
        # n = len(nums)
        # pref = [1] * ( n+1 )
        # suff = [1] * ( n+1 )
        # for i in range(1, n):
        #     if nums[i] <= nums[i-1]: pref[i] = pref[i-1] + 1 
        # for i in range(n-2, -1, -1):
        #     if nums[i] <= nums[i+1]: suff[i] = suff[i+1] + 1
        # for i in range(k, n-k):
        #     if pref[i-1] >= k and suff[i+1] >= k: ret.append(i)
        # return ret

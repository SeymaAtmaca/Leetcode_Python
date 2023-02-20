class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pos, neg = [0]*n, [0]*n
        

        if nums[0] > 0: pos[0] = 1
        if nums[0] < 0: neg[0] = 1
        ans = pos[0]

        for i in range(1, n):
            print("Pos : ", pos, " neg : ", neg)
            if nums[i] > 0 :
                pos[i] = 1 + pos[i-1]
                neg[i] = 1 + neg[i-1] if neg[i-1] > 0 else 0
            elif nums[i] < 0 : 
                pos[i] = 1 + neg[i - 1 ] if neg[i-1] > 0 else 0
                neg[i] = 1 + pos[i - 1 ] 
            ans = max(ans, pos[i])
        
        return ans
    

# asagidaki cozum daha hizli
        # ans = pos = neg = 0
        # for x in nums: 
        #     if x > 0: pos, neg = 1 + pos, 1 + neg if neg else 0
        #     elif x < 0: pos, neg = 1 + neg if neg else 0, 1 + pos
        #     else: pos = neg = 0 # reset 
        #     ans = max(ans, pos)
        # return ans
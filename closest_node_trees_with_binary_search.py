# You are given the root of a binary search tree and an array queries of size n consisting of positive integers.
# Find a 2D array answer of size n where answer[i] = [mini, maxi]:
# mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
# maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
# Return the array answer.




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        nums = []
        def inorder(node): # agactaki degerler nums array ine aktarilir
            if(node):
                inorder(node.left) # nums ın sıralı olması icin left ten right a basım yapılır
                nums.append(node.val) # right a gecmeden once mevcut deger nums a eklenir
                inorder(node.right)
        inorder(root)
        n = len(nums)
        ans = []

        for target in queries: 
            ans.append([-1, -1])
            l, r = 0, n-1
            while l <= r :
                mid = l + (r-l) // 2 # orta nokta, binary search algoritması
                if nums[mid] == target: # eger deger agacta yer alıyorsa
                    ans[-1] = [target, target] # min ve max target a esitlenir
                    break # islem tamamlanir
                elif nums[mid] > target: # eger orta nokta target tan buyukse
                    ans[-1][1] = nums[mid] # max guncellenir
                    r = mid - 1 # r ust degeri orta noktaya gore guncelenir 
                else : 
                    ans[-1][0] = nums[mid] # eger target > nums[mid] ise min nokta guncellenir
                    l = mid + 1  # binary search min elemanı l guncellenir
        return ans # elde edilen en son deger dondurulur
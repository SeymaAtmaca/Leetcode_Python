
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not len(nums):
            return None

        mid_node = len(nums) // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )


        # aşağıdaki metod yaklaşık % 30 daha hızlı 
        # if num:
        #     mid = len(num) // 2

        #     root = TreeNode(num[mid])
        #     root.left = self.sortedArrayToBST(num[0:mid])
        #     root.right = self.sortedArrayToBST(num[mid+1:len(num)+1])

        #     return root
        # else:
        #     return None
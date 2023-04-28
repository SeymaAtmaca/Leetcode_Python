# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def longest(root, right_flag, length):
            if not root: return length  # agacta kok noktalara gelindiginde hesaplanan uzunlugu dondur
            r = longest(root.right, True, length + 1 if not right_flag else 1 )     # onceki hesaplanan deger left ise 1 ekle ve right a gec
            l = longest(root.left, False, length + 1 if right_flag else 1)  # onceki hesaplanan deger right ise 1 ekle ve left e gec

            return max(r,l) # alt koke ait max degei dondur

        return max(longest(root, True, 0), longest(root, False, 0)) - 1 # en tepe root icin max uzunluk değerini don
        
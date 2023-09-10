# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, mx = 0) -> int:
        if root is None : return 0
        return (
            (1 if mx <= root.val else 0) + 
            self.goodNodes(root.left, max(root.val, mx)) + 
            self.goodNodes(root.right, max(root.val, mx))
        )
        
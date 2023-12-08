# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# def preorder(root):
#   return [root.val] + self.preorder(root.left) + self.preorder(root.right) if root else []


# def postorder(root):
#   return  self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []
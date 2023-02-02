# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sample(root):
            if not root : 
                return 0
            left_tree = sample(root.left)
            if left_tree == -1:
                return -1

            right_tree = sample(root.right)
            if right_tree == -1:
                return -1
            
            if abs(left_tree - right_tree)>1:
                return -1
            else : 
                return 1 + max(left_tree, right_tree)
        
        return sample(root)!=-1
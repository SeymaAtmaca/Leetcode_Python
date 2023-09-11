# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.calculate(root, val)
    
    def calculate(self, node, val):
        if node is None:
            return None
        
        if node.val == val:
            return node
        elif node.val < val:
            return self.calculate(node.right, val)
        else:
            return self.calculate(node.left, val)

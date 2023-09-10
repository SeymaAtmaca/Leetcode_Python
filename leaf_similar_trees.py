# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr_root1 = []
        arr_root2 = []

        self.findLeaves(root1, arr_root1)
        self.findLeaves(root2, arr_root2)

        return arr_root1 == arr_root2

    def findLeaves(self, node, arr):
        if not node:
            return
        if not node.left and not node.right:
            arr.append(node.val)
        self.findLeaves(node.left, arr)
        self.findLeaves(node.right, arr)

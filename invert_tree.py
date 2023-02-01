# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None :
            return None
        left = root.left
        right = root.right

        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root

        # ==== aşağıdaki çözüm, hız ve hafıza tüketimi açısından daha iyi 
        # if root == None:
        #     return root
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

        
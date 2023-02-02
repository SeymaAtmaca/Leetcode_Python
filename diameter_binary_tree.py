# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        def sample(root):
                if not root:
                    return 0

                left_tree_height = sample(root.left)
                right_tree_height = sample(root.right)
                self.max = max( ( left_tree_height + right_tree_height ), self.max)

                return max(left_tree_height, right_tree_height) + 1

        sample(root) 
        return self.max
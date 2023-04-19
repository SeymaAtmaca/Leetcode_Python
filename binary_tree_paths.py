# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []

        def print_tree(root, path):
            if root is None:
                return 
            if root.right == None and root.left == None:
                ret.append(''.join(path) + str(root.val))
                return 
            
            path.append(str(root.val) + '->')
            print_tree(root.left, path)
            print_tree(root.right, path)
            path.pop()
            

        print_tree(root, [])
        return ret
            
            

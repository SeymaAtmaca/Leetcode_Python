# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = defaultdict(list)
        def dfs(root,h):
            if root is None: return
            l[h].append(root.val)
            dfs(root.left, h+1)
            dfs(root.right, h+1)
        dfs(root, 1)
        res = []
        for i in l.values():
            res.append(sum(i))
        return res.index(max(res)) + 1
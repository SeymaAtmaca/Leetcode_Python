class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # s.reverse() # this is like pointer. We don't return anyting but it's also reverse outside the function
        # s[:] = s[::-1] # other option. This is faster than first one. But use a little more memory
        


solution = Solution()
string = ["h","e","l","l","o"]
result = solution.reverseString(string)
print(string)
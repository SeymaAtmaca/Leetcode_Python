class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #longest_string_length = len(max(strs, key=len))
        #ch = ( for i in range(len(strs)): for j in range(longest_string_length): if strs[i][j] == strs[])
        common = ""
        for chars in zip(*strs):
            if all(char == chars[0] for char in chars) : 
                common += chars[0]
            else:
                break

        return common

strs = ["flower","flow","flight"]
solution = Solution()
result = solution.removeDuplicates(strs)
print(result)
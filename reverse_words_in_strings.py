# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Input: s = "a good   example"
# Output: "example good a"


# runtime beast 94.84%
# memory beast 54.99%


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
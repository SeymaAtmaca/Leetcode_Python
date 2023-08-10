
# Problem açıklaması aşağıdadır. 

# Input: s = "coaching", t = "coding"
# Output: 4
# Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
# Now, t is a subsequence of s ("coachingding").
# It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i,j = 0,0
        while i < len(s) and j < len(t): 
            if s[i] == t[j] : 
                i += 1
                j += 1
            else : i += 1
        return len(t) -j
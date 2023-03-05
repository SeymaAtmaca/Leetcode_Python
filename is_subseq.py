class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sub = ""

        for i in range(len(t)):
            if t[i] in s and t[i] == s[len(sub)]:
                sub += t[i]

        return sub == s
    
# aşağıdaki yöntem daha hızlı

        # if len(t) < len(s):
        #     return False

        # last_index = 0
        # for i in range(0, len(t)):
        #     if last_index <= len(s) - 1 and s[last_index] == t[i]:
        #         last_index += 1

        # return last_index == len(s)
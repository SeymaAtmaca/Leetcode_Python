class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        val = s.split(" ")
        ret = ""

        for i in range(len(val)):
            ret += (val[i][::-1]) 
            if i != len(val)-1:
                ret += " "

        return ret

        # the following usage is faster than first one, you can use this too
        # s = s.split(" ")
        # for i in range(len(s)):
        #     s[i] = s[i][::-1]
        # return " ".join(s)

solution = Solution()
s = "Let's take LeetCode contest"
result = solution.reverseWords(s)
print(result)
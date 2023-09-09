# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret, num = "", 0
        stack = []
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append(ret)
                stack.append(num)
                ret = ""
                num = 0
            elif char == "]":
                pnum = stack.pop()
                pstr = stack.pop()
                ret = pstr + pnum * ret
            else : 
                ret += char
        return ret
        
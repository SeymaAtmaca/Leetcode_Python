class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2) : str1, str2 = str2, str1
        print("str1 : ", str1, "str2 : ", str2, "str1 + str2 : ", str1 + str2, "str2 + str1 : ", str2+ str1, "math.gcs : ", str1[:math.gcd(len(str1), len(str2))])
        if str1 + str2 != str2 + str1 : return ""
        return str1[:math.gcd(len(str1), len(str2))]
        
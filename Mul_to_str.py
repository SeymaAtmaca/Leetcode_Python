class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = int("".join([e for e in num1]))
        num2 = int("".join([e for e in num2]))
        result = num1 * num2
        return str(result)


        # ya da sadece şu saturu yazmak yeterli :)
        # return str(int(num1) * int(num2))




solution = Solution()
num1 = "2"
num2 = "3"

result = solution.multiply(num1,num2)
print("type : ", type(result), result)
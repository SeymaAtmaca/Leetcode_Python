class Solution:
    def reverseBits(self, n: int) -> int:
        binary_n = "{0:032b}".format(n)
        reversed_binary_n = binary_n[::-1]
        return int(reversed_binary_n, 2)
import math
import random
import numpy as np

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        array_list = []
        perm = math.perm(len(nums),len(nums))
        array_list.append(nums)

        while True:
            copy_numbers = nums.copy()
            random.shuffle(copy_numbers)
            
            if copy_numbers not in array_list:
                array_list.append(copy_numbers) 
            if len(array_list) == perm:

                return array_list

solution = Solution()
numbers = []
check = solution.permute(numbers)
print("len: ",len(check), "\nCheck: ",check)
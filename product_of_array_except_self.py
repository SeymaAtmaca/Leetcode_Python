# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ret = [1] * n
        left_products = [1] * n
        right_products = [1] * n
        left_product, right_product = 1,1

        for i in range(len(nums)):
            left_products[i] = left_product
            left_product *= nums[i]

            right_products[n - i - 1] = right_product
            right_product *= nums[n - i - 1]
        
        for i in range(len(nums)):
            ret[i] = left_products[i] * right_products[i]

        return ret
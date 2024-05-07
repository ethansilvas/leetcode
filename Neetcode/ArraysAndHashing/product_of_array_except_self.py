"""
solution is essentially looping forwards and backwards keeping running products

key point to remember is that we are modifying the current answer index BEFORE the running product
this way we are updating the product with every element except for itself
"""
class Solution(object):
    def productExceptSelf(self, nums):
        answer = []

        prefix = 1

        for i, num in enumerate(nums):
            answer.append(prefix)
            prefix *= num

        postfix = 1

        for i in range(len(nums) -1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer



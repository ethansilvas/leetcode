class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left = 0

        for right in range(len(nums)):
            if nums[left] != 0 and nums[right] == 0:
                left = right
                continue

            if nums[left] == 0 and nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                left += 1

        return nums

            



        
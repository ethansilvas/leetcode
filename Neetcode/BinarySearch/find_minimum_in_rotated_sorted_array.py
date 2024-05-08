class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        min_element = float('inf')

        while left <= right:
            mid = left + (right - left) // 2

            min_element = min(min_element, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return min_element

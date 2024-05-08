class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        min_num = float("inf")

        while left < right: 
            mid = left + (right - left) // 2

            min_num = min(min_num, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1 
            else:
                right = mid - 1

        # check for the case that nums[left] is the min
        # which if it is then it wouldn't have updated the min
        return min(min_num, nums[left])

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        max_average = float('-inf')

        left, right = 0, k - 1
        rolling_sum = sum(nums[left : right + 1])

        while right < len(nums):
            max_average = max(max_average, float(rolling_sum) / k)

            rolling_sum -= nums[left]
            left += 1
            right += 1

            if right < len(nums):
                rolling_sum += nums[right]

        return max_average

        
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        differences = {}

        for i, num in enumerate(nums): 
            if target - num in differences: 
                return [differences[target - num], i]

            differences[num] = i
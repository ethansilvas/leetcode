class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        unique_nums = set()

        for num in nums: 
            if num in unique_nums:
                return True
            
            unique_nums.add(num)

        return False
        
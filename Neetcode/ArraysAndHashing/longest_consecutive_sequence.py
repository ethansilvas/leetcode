"""
this will store each item in a set and loop through the set to find beginnings of sequences
then it will loop until the sequence is broken and update the longest sequence

this will remain O(N) because we always check:
    if num - 1 not in nums_set
this way, we don't waste time if the number isn't the start of a sequence

the worst-case scenario is if the whole list is a sequence and we go through the list twice
which would be O(2N) which gets reduced to O(N)
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_set = set(nums)
        longest_cons = 0

        for num in nums_set: 
            if num - 1 not in nums_set:
                current_cons = 1

                while num + current_cons in nums_set:
                    current_cons += 1

                longest_cons = max(current_cons, longest_cons)

        return longest_cons


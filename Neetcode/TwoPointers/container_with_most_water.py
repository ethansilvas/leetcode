"""
two pointer O(n) solution that uses a left (start) and right (end) poiner
move the pointers depending on which height is smaller
therefore you can find the max height by trying to find the tallest and widest containers
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # use two pointers starting from the beginning and the end of the list
        l, r = 0, len(height) - 1

        max_water = 0

        while l < r:
            # get the maximum between the current max and the current container 
            # note that the calculation for a container's water is:
            #   the shorter of the two heights * the distance between the two heights
            max_water = max(max_water, min(height[l], height[r]) * (r - l))

            # we want the tallest and longest container we can find 
            # so we will only move the lesser of our two heights
            # if the two heights are equal then we just move the left 
            if height[l] <= height[r]: 
                l += 1
            elif height[l] > height[r]:
                r -= 1

        return max_water
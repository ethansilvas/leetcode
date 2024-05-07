"""
this is an O(n^2) solution that takes advantage of sorting the array first 
with the array sorted, you can skip either: 
    positive values that we don't need to look at 
    negative values that we've already looked at 
this way we avoid submitting duplicate triplets 

for each negative value we look at, we use two pointers: 
    left pointer is the number after the value
    right pointer is the end of the list
using these two pointers we can continuously calculate the sums to try to find a valid triplet
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # sort the list to be able to use pointers to look for triplets
        nums.sort()

        triplets = []

        for i, num in enumerate(nums):
            # we don't need to look at any positive numbers because either: 
            #   we've already used all the negative numbers to find all valid triplets
            #   or there are no negatives meaning there won't be any valid triplets
            if num > 0: 
                break

            # if the current number is the same as the one before, we can skip it to avoid duplicate triplets
            if i > 0 and num == nums[i - 1]:
                continue

            # define our two pointers to look at everything after the current number
            j, k = i + 1, len(nums) - 1

            while j < k:
                # get the sum of: 
                #   current number = nums
                #   left pointer = nums[j]
                #   right pointer = nums[k]
                current_sum = num + nums[j] + nums[k]

                # reduce or increase the sums by moving our pointers
                # remember that the list is sorted so that means: 
                #   increasing the left pointer will increase the sum
                #   decreasing the right pointer will decrease the sum
                if current_sum > 0:
                    # reduce the sum by decreasing right pointer
                    k -= 1
                elif current_sum < 0:
                    # increase the sum by increasing left pointer
                    j += 1
                else: 
                    # we have found a triplet that equals 0
                    triplets.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # we still need to continue looking for triplets for the current number
                    # however, we need to do the same checks for duplicate values on the left pointer
                    # loop until the left pointer is not the same as the previous number
                    while nums[j] == nums[j - 1] and j < k: 
                        j += 1

        return triplets




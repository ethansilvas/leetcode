class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # use a 2d list where the outer index is the count 
        # and the corresponding list holds all numbers with that count
        counts = [[] for _ in range(len(nums) + 1)]
        unique_nums = {}

        # get all the unique numbers and store their counts as key:value
        for num in nums:
            if num in unique_nums:
                unique_nums[num] += 1
            else:
                unique_nums[num] = 1

        # now use index of counts list as the number of times a number was found 
        # and add num to inner list
        for num in unique_nums:
            counts[unique_nums[num]].append(num)

        top_k = []

        # loop backwards through counts list since the list goes from least frequent -> most frequent
        # REMEMBER: our end point is 0 and not -1 because there will be no value for the 0 index
        for i in range(len(counts) - 1, 0, -1):
            # add every number in the inner list to return value until k nums found
            for num in counts[i]:
                top_k.append(num)
                
                if len(top_k) == k:
                    return top_k        


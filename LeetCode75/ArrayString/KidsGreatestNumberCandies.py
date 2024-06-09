class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest_candies = 0

        for num in candies: 
            greatest_candies = max(greatest_candies, num)

        result = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest_candies:
                result[i] = True

        return result




        
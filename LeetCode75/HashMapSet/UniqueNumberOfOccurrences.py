class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        counts = {}

        for num in arr: 
            counts[num] = counts.get(num, 0) + 1

        unique_counts = set()

        for count in counts.values():
            if count in unique_counts:
                return False
            else:
                unique_counts.add(count)

        return True
        
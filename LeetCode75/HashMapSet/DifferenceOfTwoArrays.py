class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        set1 = set(nums1)
        set2 = set(nums2)

        answer = [[], []]

        for num in set1:
            if num not in set2:
                answer[0].append(num)

        for num in set2:
            if num not in set1:
                answer[1].append(num)

        return answer
        
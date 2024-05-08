class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        counts = {}
        longest_substring = 0

        left = 0
        max_frequent = 0

        for right in range(len(s)):
            # increase count of current element
            # then modify the most frequent value we have looked at
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_frequent = max(max_frequent, counts[s[right]])

            # calculate the number of characters that aren't our most frequent character
            # then compare that number to k to see how many from the left we should remove
            # make sure to update the counts before increasing left
            while (right - left + 1) - max_frequent > k:
                counts[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring


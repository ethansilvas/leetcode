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
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_frequent = max(max_frequent, counts[s[right]])

            while (right - left + 1) - max_frequent > k:
                counts[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring


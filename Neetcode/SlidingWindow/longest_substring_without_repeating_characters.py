class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0 
        longest_length = 0
        unique_chars = set()

        for right in range(len(s)):
            # if right pointer is a duplicate, move up left pointer until the right pointer isn't a duplicate anymore
            # when we move up the left pointer we need to remove it's previous value from the unique char set
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            unique_chars.add(s[right])
            longest_length = max(longest_length, right - left + 1)

        return longest_length
 
            
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        left, right = 0, len(s) - 1

        reversed = [''] * len(s)

        while left <= right:
            if s[left] not in vowels:
                reversed[left] = s[left]
                left += 1
                continue
            if s[right] not in vowels:
                reversed[right] = s[right]
                right -= 1
                continue

            reversed[left] = s[right]
            reversed[right] = s[left]
            left += 1
            right -= 1

        return ''.join(reversed)

        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left, right = 0, len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
        
'''
class Solution(object):
    def isPalindrome(self, s):
        converted_s = ""
        
        for char in s: 
            if char.isalnum():
                converted_s += char.lower()

        i, j = 0, len(converted_s) - 1

        while i < j:
            if converted_s[i] != converted_s[j]:
                return False

            i += 1
            j -= 1

        return True
'''
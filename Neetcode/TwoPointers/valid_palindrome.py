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
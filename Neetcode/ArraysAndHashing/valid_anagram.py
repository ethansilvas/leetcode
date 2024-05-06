"""
This solution uses two lists where each index maps to a character's ascii value
each time a character is found the value of it's ascii index is increased
both lists are compared to ensure that the exact same letters are used for both strings

using this solution optimizes the dictionary method because it instead will use O(1) space
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_letters = [0] * 128
        t_letters = [0] * 128

        for i in range(len(s)): 
            s_letters[ord(s[i])] += 1
            t_letters[ord(t[i])] += 1

        return s_letters == t_letters

"""
Dictionary solution

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_letters = {}

        for char in s: 
            if char in s_letters:
                s_letters[char] += 1
            else: 
                s_letters[char] = 1

        t_letters = {}

        for char in t: 
            if char not in s_letters:
                return False
            else: 
                if char in t_letters:
                    t_letters[char] += 1
                else:
                    t_letters[char] = 1

                if t_letters[char] > s_letters[char]:
                    return False

        return True
"""
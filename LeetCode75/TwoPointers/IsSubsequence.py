class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_pointer, t_pointer = 0, 0


        while s_pointer < len(s) and t_pointer < len(t):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1

            t_pointer += 1

        return s_pointer >= len(s)
        
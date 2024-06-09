class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        loop backwards through the minimum length string 
        for each substring length you are currently on: 
            check to see if that both strings are divisible by that length
            if they are divisible: 
                store each quotient of (len(str1) / substring_len) and (len(str2) / substring_len)
                multiply the substring by these quotients to see if they replicate str1 and str2 respectively
                    thus meaning that the substring multiplied by the quotient will result in str1 = substr + substr ...
        """

        len1, len2 = len(str1), len(str2)

        def is_divisor(substr_len):
            if len1 % substr_len != 0 or len2 % substr_len != 0:
                return False

            factor1, factor2 = len1 / substr_len, len2 / substr_len

            return str1[:substr_len] * factor1 == str1 and str1[:substr_len] * factor2 == str2

        for substr_len in range(min(len1, len2), 0, -1):
            if is_divisor(substr_len):
                return str1[:substr_len]

        return ""
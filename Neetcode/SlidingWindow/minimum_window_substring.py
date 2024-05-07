class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # initialize our dictionaries to hold: 
        #   the counts of each character in t
        #   the current substring of letters we are using and their counts
        t_counts, current_counts = {}, {}

        # initialize the t_counts dictionary
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        # keep track of how many characters of t we have satisfied
        # meaning, we have found as many of each character that we need
        # ex: t = "ABBC" and we've found 1 a, 2 b, and 1 c
        #   so therefore our have count would be 3 because we satisfied all conditions
        have = 0

        # store how many unique characters we need to find all the counts for
        need = len(t_counts)

        min_substring, min_substring_length = [-1, -1], float("infinity")

        left = 0

        for right in range(len(s)):
            # store the current character and update it's count in our current dictionary
            current_char = s[right]
            current_counts[current_char] = current_counts.get(current_char, 0) + 1

            # check if the current char is one of the required chars in t_counts
            # then also check if we have reached the required count
            #   if we have reached the required count then update our have count
            if current_char in t_counts and current_counts[current_char] == t_counts[current_char]:
                have += 1

            # now we check to see if we have found all the required characters, and the correct amounts of those characters
            # if we have, we want to then find the minimum length of substring where this condition is still valid
            # to do this we can start increasing our left pointer until we don't have all the characters we need
            while have == need:
                if (right - left + 1) < min_substring_length:
                    min_substring = [left, right]
                    min_substring_length = right - left + 1

                # before we increment the left pointer we need to decrement its count
                current_counts[s[left]] -= 1

                # when we decrement its count we also need to check if that means we no longer have all the chars we need
                if s[left] in t_counts and current_counts[s[left]] < t_counts[s[left]]:
                    have -= 1
                
                # then after performing the above checks we can then increment the left pointer 
                # to try to find the smallest substring we can 
                left += 1

        # unpack our result pointers to get the substring
        left, right = min_substring

        if min_substring_length == float("infinity"):
            return ''
        else:
            return s[left:right + 1]
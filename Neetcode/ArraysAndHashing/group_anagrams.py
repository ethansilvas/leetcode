"""
This solution uses a list as an ascii table to then convert into a tuple
the tuple will be used as a key to a dictionary where the values are the list of words that are anagrams

this will only be O(M * N) time where M = number of words and N = length of a given word 
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        grouped_anagrams = {}

        for word in strs:
            # create an ascii table of all lowercase letters to map each character to its count
            letters = [0] * 26

            for letter in word: 
                letters[ord(letter) - ord('a')] += 1

            # this will be O(1) time because it has a fixed length of 26
            letters = tuple(letters)

            if letters in grouped_anagrams:
                grouped_anagrams[letters].append(word)
            else: 
                grouped_anagrams[letters] = [word]

        return grouped_anagrams.values()

"""
This solution uses sorting which will be O(nlogn)
which would make the total time complexity O(N * MlogM)
where N = number of strings and M = length of a given string

class Solution(object):
    def groupAnagrams(self, strs):
        grouped_anagrams = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in grouped_anagrams:
                grouped_anagrams[sorted_word].append(word)
            else: 
                grouped_anagrams[sorted_word] = [word]

        return grouped_anagrams.values()
"""


        
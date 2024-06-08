class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        p1, p2 = 0, 0

        counter = 0

        merged = []

        while p1 < len(word1) and p2 < len(word2):
            if counter % 2 == 0:
                merged.append(word1[p1])
                p1 += 1
            else:
                merged.append(word2[p2])
                p2 += 1

            counter += 1

        if not p1 < len(word1):
            merged.extend(word2[p2:])
        else:
            merged.extend(word1[p1:])

        return ''.join(merged)


        
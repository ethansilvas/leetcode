class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True

        planted = 0

        for i in range(len(flowerbed)):
            if planted >= n:
                return True

            if (i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0) or (
                i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0):
                flowerbed[i] = 1
                planted += 1
                continue

            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                planted += 1
            
        return planted >= n


        
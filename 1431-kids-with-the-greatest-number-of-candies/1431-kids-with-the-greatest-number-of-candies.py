class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result =[]
        for i in candies:
            i =i + extraCandies
            if i >=max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


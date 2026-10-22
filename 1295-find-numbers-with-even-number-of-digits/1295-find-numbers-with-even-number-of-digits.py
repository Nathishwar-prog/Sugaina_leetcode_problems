class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result =[]
        count = 0
        for i in range(len(nums)):
            result.append(len(str(nums[i])))
            if result[i]%2 == 0:
                count +=1
        return count

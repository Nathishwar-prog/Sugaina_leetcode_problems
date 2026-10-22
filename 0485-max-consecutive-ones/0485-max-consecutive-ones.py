class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            elif nums[i]==0:
                result.append(count)
                count =0
        result.append(count)
        return max(result)
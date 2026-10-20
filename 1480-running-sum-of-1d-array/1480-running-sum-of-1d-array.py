class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        for i in range(len(nums)):
            if runningSum == []:
                runningSum.append(nums[i])
            else:
                runningSum.append(nums[i] + runningSum[i-1])
        return runningSum
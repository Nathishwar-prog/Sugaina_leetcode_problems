class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_numbers = set(nums)
        if len(unique_numbers) < len(nums):
            return True
        else:
            return False


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = x
        result = 0
        while x > 0:
            digit = x%10
            result = result*10 + digit
            x = x//10

        if original == result:
            return True
        else:
            return False

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        value = ""
        for i in digits:
            value = value + str(i)
        integervalue = int(value) + 1
        string = str(integervalue)
        result =[]
        for i in range(len(string)):
            result.append(int(string[i]))
        return result




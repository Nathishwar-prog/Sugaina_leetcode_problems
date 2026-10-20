class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        value =[]
        for i in range(len(accounts)):
            data = 0
            for j in range(len(accounts[i])):
               data += accounts[i][j]
            value.append(data)
        return max(value)

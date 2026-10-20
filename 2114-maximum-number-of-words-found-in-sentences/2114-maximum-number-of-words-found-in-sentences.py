class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        words = []
        for i in sentences:
            i=i.split(" ")
            words.append(len(i))
        return max(words)